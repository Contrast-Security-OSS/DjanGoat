# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Retirement(models.Model):
    """
    Class defining the Retirement model

    t.string   "total",            limit: 255
    t.string   "employee_contrib", limit: 255
    t.string   "employer_contrib", limit: 255
    t.integer  "user_id",          limit: 4
    t.datetime "created_at"
    t.datetime "updated_at"
    """
    MAX_INT_VALUE = 2**32-1

    def __str__(self):
        return self.user.__str__() + " Retirement Summary: \n" \
               + "\nTotal: " + str(self.total) \
               + "\nEmployee Contribution: " + str(self.employee_contrib) \
               + "\nEmployer Contribution: " + str(self.employer_contrib)

    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             related_name="retirements")
    total = models.CharField(max_length=255)
    employee_contrib = models.CharField(max_length=255)
    employer_contrib = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_retirements"
