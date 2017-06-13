# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator


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

    @staticmethod
    def __authenticate(input_email, input_password):
        auth = None
        user = find_by_email(input_email)

        if user.password == input_password:
            auth = user
        else:
            print("Incorrect Password!")

        return auth


def find_by_email(input_email):
    """
    Finds a user by email.
    :param input_email: The email of the user being searched for
    :return: the user with an email matching input_email
    """
    return User.objects.filter(email=input_email).first()

