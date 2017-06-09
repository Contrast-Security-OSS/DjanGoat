# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import KeyManagement
from app.tests.mixins import ModelCrudTests


class KeyManagementModelTests(TestCase, ModelCrudTests):

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

        # Create KeyManagement Model
        input_iv = "my_iv"
        km_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        km_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.model = KeyManagement.objects.create(
            iv=input_iv, user_id = self.parent,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )
        self.model.save()

        self.model_update_attribute = "iv"
        self.model_update_input = "iv2"



