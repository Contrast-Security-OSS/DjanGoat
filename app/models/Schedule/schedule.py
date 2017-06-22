# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import json


@python_2_unicode_compatible
class Schedule(models.Model):
    """
    Class defining the Schedule model

    t.string   "event_type", limit: 255
    t.date     "date_begin"
    t.date     "date_end"
    t.string   "event_name", limit: 255
    t.string   "event_desc", limit: 255
    t.integer  "user_id",    limit: 4
    t.datetime "created_at"
    t.datetime "updated_at"
    """

    def __str__(self):
        return self.user.__str__() + " Schedule Summary: \n" \
            + "\nEvent Type: " + str(self.event_type) \
            + "\nEvent Name: " + str(self.event_name) \
            + "\nEvent Description: " + str(self.event_desc) + "\n"

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    pto = models.ForeignKey('PaidTimeOff', on_delete=models.CASCADE,
                            blank=True, null=True)
    date_begin = models.DateField()
    date_end = models.DateField()
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    event_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "app_schedules"

    # Take MM/DD/YYYY and return YYYY-MM-DD
    @staticmethod
    def reformat(s):
        M, D, Y = s.split('/')
        return Y + '-' + M + '-' + D

    # Take list of schedules and turn them into JSON list for calendar
    @staticmethod
    def to_calendar(schedules):
        event_list = [{"title": str(event.event_name),
                       "start": str(event.date_begin),
                       "end": str(event.date_end)} for event in schedules]
        return json.dumps(event_list)
