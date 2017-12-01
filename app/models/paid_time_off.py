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
        return self.user.__str__() + " PTO Summary: \n" \
            + "\nSick Days Taken: " + str(self.sick_days_taken) \
            + "\nSick Days Earned: " + str(self.sick_days_earned) \
            + "\nPTO Taken: " + str(self.pto_taken) \
            + "\n PTO Earned: " + str(self.pto_earned)

    sick_days_taken = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    sick_days_earned = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    pto_taken = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    pto_earned = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             related_name='pto')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_paid_time_offs"

    def sick_days_remaining(self):
        return self.sick_days_earned - self.sick_days_taken

    def pto_days_remaining(self):
        return self.pto_earned - self.pto_taken

    def sick_days_taken_percentage(self):
        return float(self.sick_days_taken)/float(self.sick_days_earned)*100.0

    @staticmethod
    def validate_PTO_form(form):
        err_list = []
        if len(form['event_name']) == 0:
            err_list.append('Event Name cannot be empty')
        if len(form['event_description']) == 0:
            err_list.append('Event Description cannot be empty')
        if len(form['date_begin']) == 0:
            err_list.append('Event Dates cannot be empty')
        err_msg = " and ".join(err_list)
        return err_msg
