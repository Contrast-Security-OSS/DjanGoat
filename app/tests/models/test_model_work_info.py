# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import KeyManagement
from app.models import WorkInfo
from app.tests.mixins import ModelCrudTests, Pep8ModelTests
from Crypto import Random
import binascii


class WorkInfoModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
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

        # Create WorkInfo Model
        input_income = "fun"
        input_bonuses = "birthday"
        input_years_worked = 10
        input_ssn = "111-22-3333"
        input_encrypted_ssn = "random_chars".encode("utf-8")
        input_dob = datetime.date(1996, 7, 31)
        perf_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        perf_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.model = WorkInfo.objects.create(
            income=input_income,
            bonuses=input_bonuses,
            years_worked=input_years_worked,
            SSN=input_ssn,
            encrypted_ssn=input_encrypted_ssn,
            DoB=input_dob,
            created_at=perf_input_create_date,
            updated_at=perf_input_update_date,
            user=self.parent,
        )

        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        km_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.parent,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        # Model attributes to be updated
        self.attributes = ["user", "income", "bonuses",
                           "years_worked", "SSN", "encrypted_ssn",
                           "DoB", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "102544"

        # File path for pep8 tests
        self.path = "app/models/WorkInfo/work_info.py"

    def test_encrypt_decrypt(self):
        self.model.encrypt_ssn()
        self.assertEquals("111-22-3333", self.model.decrypt_ssn())

    # Override
    def test_delete_user_and_pto(self):
        """Test to ensure Model is deleted when its parent is deleted.
        """
        if self.parent is not None:
            response = self.parent.delete()
            num_objects_deleted = response[0]
            '''2 objects deleted from database'''
            self.assertEqual(num_objects_deleted, 3)

            self.assertIsNone(self._get_from_db(self.parent), "Parent not deleted from the database")
            self.assertIsNone(self._get_from_db(self.model), "Model not deleted from database with cascade")
        else:
            pass
