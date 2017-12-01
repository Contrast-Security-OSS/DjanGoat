# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class KeyManagement(models.Model):
    """
    Class defining the KeyManagement model
    """

    def __str__(self):
        return self.iv + " for user " + self.user.__str__()

    # needs to be a 16byte string use -> binascii.hexlify(Random.new().read(8))
    iv = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def work_info(self):
        from app.models.work_info import WorkInfo
        return WorkInfo.object.get(self.user)

    class Meta:
        db_table = "app_key_managements"
