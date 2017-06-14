# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from . import user_data
import random
from app.models import Retirement


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
        index = random.randint(0,3)
        # Tuple of form ("employee_contrib", "employer_contrib", "total")
        retirement = Retirement(employee_contrib=user_data.retirement_data[index][0],
                                employer_contrib=user_data.retirement_data[index][1],
                                total=user_data.retirement_data[index][2],
                                user_id=self, created_at=user_data.date_one,
                                updated_at=user_data.date_three)

    @staticmethod
    def authenticate(input_email, input_password):
        user = find_by_email(input_email)

        if user.password == input_password:
            auth = user
        else:
            raise Exception("Incorrect Password!")
        return auth


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
