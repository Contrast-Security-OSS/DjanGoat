# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import PaidTimeOff
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class UserModelTests(TestCase, ModelCrudTests, Pep8ModelTests):

    def setUp(self):
        # Create the user
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))

        self.parent = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        # Create PTO Model
        input_sick_days_earned = 20
        input_sick_days_taken = 2
        input_pto_days_earned = 10
        input_pto_days_taken = 4
        pto_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 4, 0, 0))
        pto_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 5, 0, 0))

        # Model being tested
        self.model = PaidTimeOff.objects.create(
            sick_days_earned=input_sick_days_earned,
            sick_days_taken=input_sick_days_taken,
            pto_earned=input_pto_days_earned,
            pto_taken=input_pto_days_taken,
            created_at=pto_input_create_date,
            updated_at=pto_input_update_date,
            user=self.parent
        )

        # Model attributes to be updated
        self.attributes = ["user", "sick_days_earned", "sick_days_taken",
                           "pto_earned", "pto_taken", "created_at",
                           "updated_at"]
        self.model_update_index = 4
        self.model_update_input = 5

        # Path for pep8 tests
        self.path = "app/models/PaidTimeOff/paid_time_off.py"

    def test_sick_days_remaining(self):
        pto = PaidTimeOff.objects.get(user=self.parent)
        self.assertEqual(pto.sick_days_remaining(), 18)

    def test_pto_days_remaining(self):
        pto = PaidTimeOff.objects.get(user=self.parent)
        self.assertEqual(pto.pto_days_remaining(), 6)

    def test_sick_days_taken_percentage(self):
        pto = PaidTimeOff.objects.get(user=self.parent)
        self.assertEqual(pto.sick_days_taken_percentage(), 10.0)
