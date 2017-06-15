# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import KeyManagement
from app.tests.mixins import ModelCrudTests, Pep8ModelTests
from Crypto import Random
import binascii


class KeyManagementModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
    def setUp(self):
        # Create the user
        input_email = "ryan.dens@contrastsecurity.com"
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
        self.parent.save()

        # Create KeyManagement Model
        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        km_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.model = KeyManagement.objects.create(
            iv=input_iv, user_id=self.parent,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )
        self.model.save()

        # Model attributes to be updated
        self.attributes = ["user_id", "iv", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "iv2"

        # Path for pep8 tests
        self.path = "app/models/KeyManagement/key_management.py"
