# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Message(models.Model):
    MAX_MESSAGE_LEN = 65535
    creator_id = models.PositiveIntegerField()
    receiver_id = models.PositiveIntegerField()
    message = models.TextField(max_length=MAX_MESSAGE_LEN)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_messages"
