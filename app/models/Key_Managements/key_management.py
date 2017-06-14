# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from app.models import WorkInfo


@python_2_unicode_compatible
class KeyManagement(models.Model):
    """
    Class defining the KeyManagement model
    """

    def __str__(self):
        return self.iv + " for user " + self.user_id.__str__()

    iv = models.CharField(
        max_length=255)  # needs to be a 16byte string so please use binascii.hexlify(Random.new().read(8))
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def work_info(self):
        return WorkInfo.object.get(self.user_id)

    class Meta:
        db_table = "app_key_managements"
