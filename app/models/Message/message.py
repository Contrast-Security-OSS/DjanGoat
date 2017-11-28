# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.models.User.user import User
from django.utils import safestring


class Message(models.Model):
    MAX_MESSAGE_LEN = 65535
    creator = models.ForeignKey('User', on_delete=models.CASCADE,
                                related_name="created_messages")
    receiver = models.ForeignKey('User', on_delete=models.CASCADE,
                                 related_name="received_messages")
    message = models.TextField(max_length=MAX_MESSAGE_LEN)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_messages"

    def creator_name(self):
        creator = User.objects.filter(user_id=self.creator_id).first()
        if creator is not None:
            return creator.full_name()
        else:
            return safestring.mark_safe("<b>Name unavailable</b>")
