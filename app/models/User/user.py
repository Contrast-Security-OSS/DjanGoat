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
    def __str__(self):
        return self.first_name + " " + self.last_name

    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_id = models.IntegerField(validators=[MaxValueValidator(4)])
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    auth_token = models.CharField(max_length=255)

