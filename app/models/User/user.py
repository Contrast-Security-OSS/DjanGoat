# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from . import user_data
import random
import datetime
import pytz
from app.models.Retirement.retirement import Retirement
from app.models.PaidTimeOff.paid_time_off import PaidTimeOff
from app.models.Schedule.schedule import Schedule
from app.models.WorkInfo.work_info import WorkInfo
from app.models.Performance.performance import Performance


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

    def __str__(self):
        return self.first_name + " " + self.last_name

    def build_benefits_data(self):
        # index of the data being chosen
        index = random.randint(0, 3)

        # Tuple of form ("employee_contrib", "employer_contrib", "total")
        retirement = Retirement.objects.create(
            employee_contrib=user_data.retirement_data[index][0],
            employer_contrib=user_data.retirement_data[index][1],
            total=user_data.retirement_data[index][2], user_id=self,
            created_at=user_data.date_one, updated_at=user_data.date_three)

        # ("sick_days_taken", "sick_days_earned", "pto_taken", "pto_earned")
        pto = PaidTimeOff.objects.create(
            sick_days_taken=user_data.pto_data[index][0],
            sick_days_earned=user_data.pto_data[index][1],
            pto_taken=user_data.pto_data[index][2],
            pto_earned=user_data.pto_data[index][3],
            user_id=self, created_at=user_data.date_two,
            updated_at=user_data.date_three
        )

        # # ("event_type", "event_desc", "event_name")
        schedule = Schedule.objects.create(
            date_begin=user_data.date_three,
            date_end=user_data.date_four,
            event_type=user_data.schedule_data[index][0],
            event_desc=user_data.schedule_data[index][1],
            event_name=user_data.schedule_data[index][2],
            user_id=self, created_at=user_data.date_one,
            updated_at=user_data.date_two
        )

        # ("income", "bonuses", years_worked, "SSN", "DoB")
        # work_info = WorkInfo.objects.create(
        #     income=user_data.work_info_data[index][0],
        #     bonuses=user_data.work_info_data[index][1],
        #     years_worked=user_data.work_info_data[index][2],
        #     SSN=user_data.work_info_data[index][3],
        #     DoB=user_data.work_info_data[index][4],
        #     user_id=self, created_at=user_data.date_two,
        #     updated_at=user_data.date_two
        # )

        # ("reviewer", "comments", date_submitted, score)
        # performance = Performance(
        #     reviewer=user_data.reviewer,
        #     comments=user_data.performance_data[index][0],
        #     date_submitted=user_data.performance_data[index][1],
        #     score=user_data.pto_data[index][2],
        #     user_id=self, created_at=user_data.date_three,
        #     updated_at=user_data.date_four)

        # print(retirement, pto, schedule, work_info)

    @staticmethod
    def authenticate(input_email, input_password):
        user = User.find_by_email(input_email)

        if user.password == input_password:
            auth = user
        else:
            raise Exception("Incorrect Password!")
        return auth

    @staticmethod
    def find_by_email(input_email):
        """
        Finds a user by email.
        :param input_email: The email of the user being searched for
        :return: the user with an email matching input_email
        """
        try:
            return User.objects.filter(email=input_email).first()
        except User.DoesNotExist:
            print("User does not exist!")