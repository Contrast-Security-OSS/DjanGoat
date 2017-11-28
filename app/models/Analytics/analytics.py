# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models, connection
import re


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

    class Meta:
        db_table = "app_analytics"

    @classmethod
    def objects_in_list(cls):
        objects = cls.objects.all()
        cols = ['ip_address', 'referrer', 'user_agent',
                'created_at', 'updated_at']
        formated = dict()
        for col in cols:
            formated[col] = [getattr(item, col) for item in objects]
        return formated

    @staticmethod
    def format_raw_sql(cmd, raw, col):
        try:
            if col == '*':
                cols = ['ip_address', 'referrer', 'user_agent',
                        'created_at', 'updated_at']
            else:
                cols = re.search('SELECT (.+?) FROM', cmd).group(1)
                cols = cols.split(', ')
            num_cols = len(cols)
            formatted = dict()
            for i in range(num_cols):
                formatted[cols[i]] = [item[i] for item in raw]
            return formatted
        except:
            return dict()

    @classmethod
    def hits_by_ip(cls, ip, col='*'):
        table_name = cls.objects.model._meta.db_table
        cmd = "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC" % (
            col, table_name, ip)
        with connection.cursor() as cursor:
            cursor.execute(cmd)
            raw = cursor.fetchall()
        formatted = Analytics.format_raw_sql(cmd, raw, col)
        return formatted

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
