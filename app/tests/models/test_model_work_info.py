# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import WorkInfo
from app.tests.mixins import ModelCrudTests, Pep8ModelTests



class WorkInfoModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
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

        # Create WorkInfo Model
        input_income = "fun"
        input_bonuses = "birthday"
        input_years_worked = 10
        input_ssn = "12345"
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
            user_id=self.parent,
        )
        self.model.save()

        # Model attributes to be updated
        self.attributes = ["user_id", "income", "bonuses",
                           "years_worked", "SSN", "encrypted_ssn",
                           "DoB", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "102544"

        # File path for pep8 tests
        self.path = "app/models/WorkInfo/work_info.py"
