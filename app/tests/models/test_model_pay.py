# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django imports
from django.test import TestCase
from django.utils import timezone
# App imports
from app.tests.mixins import ModelCrudTests, Pep8ModelTests
from app.models import User, Pay, KeyManagement
# Other imports
from Crypto import Random
import datetime
import pytz
import binascii


class PayModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
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

        # Create Pay Model
        input_bank_acc_num = "123456789"
        input_bank_route_num = "54321"
        input_perc_deposit = 55
        pay_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        pay_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = timezone.now()
        km_input_update_date = timezone.now()

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.parent,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        self.model = Pay.objects.create(
            bank_account_num=input_bank_acc_num,
            bank_routing_num=input_bank_route_num,
            percent_of_deposit=input_perc_deposit,
            created_at=pay_input_create_date,
            updated_at=pay_input_update_date,
            user=self.parent
        )

        # Model attributes to be updated
        self.attributes = ["user", "bank_account_num", "bank_routing_num",
                           "percent_of_deposit", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "123454321"

        # Path for pep8 tests
        self.path = "app/models/Pay/pay.py"
