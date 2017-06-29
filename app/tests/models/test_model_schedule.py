# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import Schedule
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class ScheduleModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
    def setUp(self):

        # Create the user
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))

        self.parent = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        # Create Schedule Model
        input_event_type = "fun"
        input_event_name = "birthday"
        input_event_desc = "12345"
        input_date_begin = datetime.date(2017, 7, 31)
        input_date_end = datetime.date(2017, 8, 1)
        perf_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        perf_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.model = Schedule.objects.create(
            event_type=input_event_type,
            event_name=input_event_name,
            event_desc=input_event_desc,
            date_begin = input_date_begin,
            date_end = input_date_end,
            created_at=perf_input_create_date,
            updated_at=perf_input_update_date,
            user=self.parent,
        )

        # Model attributes to be updated
        self.attributes = ["user", "event_type", "event_name",
                           "event_desc", "date_begin", "date_end",
                           "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "102544"

        # Path to file for pep8 tests
        self.path = "app/models/Schedule/schedule.py"
