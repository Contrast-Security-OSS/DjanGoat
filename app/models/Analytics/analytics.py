# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Analytics(models.Model):
    """
       Class defining the Analytics model
    """

    def __str__(self):
        return self.referrer + " " + self.ip_address

    ip_address = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

