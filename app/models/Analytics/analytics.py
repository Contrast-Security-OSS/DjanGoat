# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models, connection
from app.models import User
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

    @staticmethod
    def format_raw_sql(cmd, raw):
        try:
            cols = re.search('SELECT (.+?) FROM', cmd).group(1)
            cols = cols.split(',')
            num_cols = len(cols)
            formated = dict()
            for (col, i) in (cols, range(num_cols)):
                col_values = []
                for item, j in raw, range(num_cols):
                    col_values.append(item[i][j])
                formated.update({col: col_values})
            print(formated)
        except Exception as e:
            print(e)

    @classmethod
    def hits_by_ip(cls, ip, col='*'):
        # raw method requires a primary key
        if (col != '*'):
            col = 'id, ' + col
        table_name = cls.objects.model._meta.db_table
        cmd = "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC" % (
            col, table_name, ip)
        with connection.cursor() as cursor:
            cursor.execute(cmd)
            raw = cursor.fetchall()
        formated = Analytics.format_raw_sql(cmd, raw)
        return cls.objects.raw(
            "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC"
            % (col, table_name, ip))

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
