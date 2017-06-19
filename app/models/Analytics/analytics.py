# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from app.models import User


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

    @classmethod
    def hits_by_ip(cls, ip, col='*'):
        # raw method requires a primary key
        if (col != '*'):
            col = 'id, ' + col
        table_name = cls.objects.model._meta.db_table
        objects = cls.objects.raw(
            "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC"
            % (col, table_name, ip))
        # if (col != '*'):
        #     cols = col.split(',')
        #     cols[0] = 'ip_address'
        #     result =
        return objects

    # defined in railsgoat but not used, expects valid column name
    @classmethod
    def count_by_col(cls, col):
        return cls.objects.values(col).count()

    # expects field type to be string
    @staticmethod
    def parse_field(field):
        valid_fields = ["ip_address", "referrer", "user_agent"]
        if field in valid_fields:
            return field
        else:
            return '1'
