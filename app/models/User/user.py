# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import random

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe

from app.models.PaidTimeOff.paid_time_off import PaidTimeOff
from app.models.Performance.performance import Performance
from app.models.Retirement.retirement import Retirement
from app.models.Schedule.schedule import Schedule
from app.models.WorkInfo.work_info import WorkInfo
from . import user_data


@python_2_unicode_compatible
class User(models.Model):
    """
    Class defining the User model
    """
    MAX_USER_ID_VALUE = 2 ** 32 - 1

    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_USER_ID_VALUE)]
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    auth_token = models.CharField(max_length=255)

    def build_benefits_data(self):
        # index of the data being chosen
        index = random.randint(0, 3)

        # Tuple of form ("employee_contrib", "employer_contrib", "total")
        Retirement.objects.create(
            employee_contrib=user_data.retirement_data[index][0],
            employer_contrib=user_data.retirement_data[index][1],
            total=user_data.retirement_data[index][2], user=self,
            created_at=user_data.date_one, updated_at=user_data.date_three)

        # ("sick_days_taken", "sick_days_earned", "pto_taken", "pto_earned")
        PaidTimeOff.objects.create(
            sick_days_taken=user_data.pto_data[index][0],
            sick_days_earned=user_data.pto_data[index][1],
            pto_taken=user_data.pto_data[index][2],
            pto_earned=user_data.pto_data[index][3],
            user=self, created_at=user_data.date_two,
            updated_at=user_data.date_three
        )

        # ("event_type", "event_desc", "event_name")
        Schedule.objects.create(
            date_begin=user_data.date_three,
            date_end=user_data.date_four,
            event_type=user_data.schedule_data[index][0],
            event_desc=user_data.schedule_data[index][1],
            event_name=user_data.schedule_data[index][2],
            user=self, created_at=user_data.date_one,
            updated_at=user_data.date_two
        )

        # ("income", "bonuses", years_worked, "SSN", "DoB")
        WorkInfo.objects.create(
            income=user_data.work_info_data[index][0],
            bonuses=user_data.work_info_data[index][1],
            years_worked=user_data.work_info_data[index][2],
            SSN=user_data.work_info_data[index][3],
            DoB=user_data.work_info_data[index][4],
            user=self, created_at=user_data.date_two,
            updated_at=user_data.date_two
        )

        reviewer = User.objects.create(
            user_id=user_data.reviewer_data[0],
            email=user_data.reviewer_data[1],
            password=user_data.reviewer_data[2],
            is_admin=user_data.reviewer_data[3],
            first_name=user_data.reviewer_data[4],
            last_name=user_data.reviewer_data[5],
            created_at=user_data.reviewer_data[6],
            updated_at=user_data.reviewer_data[7],
            auth_token=user_data.reviewer_data[8]
        )

        # ("reviewer", "comments", date_submitted, score)
        Performance.objects.create(
            reviewer=reviewer,
            comments=user_data.performance_data[index][0],
            date_submitted=user_data.performance_data[index][1],
            score=user_data.pto_data[index][2],
            user=self, created_at=user_data.date_three,
            updated_at=user_data.date_four)

    @staticmethod
    def authenticate(input_email, input_password):
        user = User.find_by_email(input_email)
        if user is not None:
            if user.password == hashlib.md5(input_password.encode()).hexdigest():
                auth = user
            else:
                raise Exception("Incorrect Password!")
            return auth
        else:
            raise User.DoesNotExist

    @staticmethod
    def authenticate_by_token(input_auth_token):
        user = User.objects.filter(auth_token=input_auth_token).first()
        return user

    def assign_user_id(self):
        if self.user_id != None:
            return
        # User with highest id
        user = User.objects.order_by("-user_id").first()
        if user is not None:
            # Set the new user's id to be one higher
            self.user_id = user.user_id + 1
        else:
            self.user_id = 1

    def hash_password(self):
        if self.password is not None:
            hash_obj = hashlib.md5(self.password.encode())
            self.password = hash_obj.hexdigest()

    def generate_token(self):
        """
        Generates and sets an auth token for a user.
        :return: None
        """
        self.auth_token = hashlib.md5((self.email + str(random.randint(1,1000000))).encode()).hexdigest()

    @staticmethod
    def find_by_email(input_email):
        """
        Finds a user by email.
        :param input_email: The email of the user being searched for
        :return: the user with an email matching input_email
        """
        return User.objects.filter(email=input_email).first()

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def safe_name(self):
        return mark_safe(self.first_name)

    @staticmethod
    def validate_signup_form(form):
        err_list = []
        if len(form["password"]) < 6:
            err_list.append("Password minimum 6 characters")
        if len(form["password"]) > 40:
            err_list.append("Password maximum 40 characters")
        if form["password"] != form["confirm"]:
            err_list.append("Password and Confirm Password does not match")
        if User.objects.filter(email=form["email"]):
            err_list.append("Email has already been taken")
        err_msg = " and ".join(err_list)
        return err_msg

    @staticmethod
    def validate_update_form(form, user, update):
        err_list = []
        if form["password_new"] != form["confirm"]:
            err_list.append("Password and Confirm Password does not match")
        elif len(form["password_new"]) != 0:
            if len(form["password_new"]) < 6:
                err_list.append("Password minimum 6 characters")
            elif len(form["password_new"]) > 40:
                err_list.append("Password maximum 40 characters")
            else:
                update["password"] = form["password_new"]
        if len(form["email_new"]) > 0:
            if User.objects.filter(email=form["email_new"]):
                if user.email != form["email_new"]:
                    err_list.append("Email has already been taken")
            else:
                update["email"] = form["email_new"]
        if len(form["first_name"]) > 0 and user.first_name != form["first_name"]:
            update["first_name"] = form["first_name"]
        if len(form["last_name"]) > 0 and user.last_name != form["last_name"]:
            update["last_name"] = form["last_name"]
        err_msg = " and ".join(err_list)
        return err_msg

    def __str__(self):
        return "User is: " + self.full_name()
