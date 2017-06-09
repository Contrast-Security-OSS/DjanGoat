# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator



@python_2_unicode_compatible
class PaidTimeOff(models.Model):
    """
    Class defining the PaidTimeOff model
    """
    MAX_INT_VALUE = 2**32-1

    def __str__(self):
        return self.user_id.__str__() + " PTO Summary: \n" \
               + "\nSick Days Taken: " + str(self.sick_days_taken) \
               + "\nSick Days Earned: " + str(self.sick_days_earned) \
               + "\nPTO Taken: " + str(self.pto_taken) \
               + "\n PTO Earned: " + self.pto_earned

    sick_days_taken = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_INT_VALUE)])
    sick_days_earned = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_INT_VALUE)])
    pto_taken = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_INT_VALUE)])
    pto_earned = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_INT_VALUE)])
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_paid_time_offs"
