# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import PaidTimeOff
from app.tests.mixins import ModelCrudTests


class UserModelTests(TestCase, ModelCrudTests):

    def setUp(self):

        # Create the user
        input_user_id = 1
        input_email = "ryan.dens@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        input_auth_token = "test"

        self.parent = User.objects.create(
            user_id=input_user_id,
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date, auth_token=input_auth_token
        )
        self.parent.save()

        # Create PTO Model
        input_sick_days_earned = 20
        input_sick_days_taken = 2
        input_pto_days_earned = 10
        input_pto_days_taken = 4
        pto_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        pto_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        # Model being tested
        self.model = PaidTimeOff.objects.create(
            sick_days_earned=input_sick_days_earned,
            sick_days_taken=input_sick_days_taken,
            pto_earned=input_pto_days_earned,
            pto_taken=input_pto_days_taken,
            created_at=pto_input_create_date,
            updated_at=pto_input_update_date,
            user_id=self.parent
        )
        self.model.save()

        # Model attribute to be updated
        self.model_update_attribute = "sick_days_taken"
        self.model_update_input = 5