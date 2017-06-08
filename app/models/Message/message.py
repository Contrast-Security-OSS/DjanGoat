# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Message(models.Model):
    MIN_USER_ID_VALUE = 0
    MAX_USER_ID_VALUE = 2 ** 32 - 1
    MAX_MESSAGE_LEN = 65535
    creator_id = models.IntegerField(validators=[MinValueValidator(MIN_USER_ID_VALUE),
                                                 MaxValueValidator(MAX_USER_ID_VALUE)])
    receiver_id = models.IntegerField(validators=[MinValueValidator(MIN_USER_ID_VALUE),
                                                 MaxValueValidator(MAX_USER_ID_VALUE)])
    message = models.TextField(max_length = MAX_MESSAGE_LEN)
    read = models.BooleanField(default = False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
