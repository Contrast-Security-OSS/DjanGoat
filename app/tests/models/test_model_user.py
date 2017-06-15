# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User, Retirement, PaidTimeOff, Schedule, WorkInfo, Performance
from app.tests.mixins import ModelCrudTests


class UserModelTests(TestCase, ModelCrudTests):
    user = None
    input_email = None
    input_password = None
    input_admin = None
    input_first_name = None
    input_last_name = None
    input_create_date = None
    input_update_date = None
    input_auth_token = None

    def setUp(self):
        # Path to file of model
        self.path = "app/models/User/user.py"
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

        self.model = User.objects.create(
            user_id=input_user_id,
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date, auth_token=input_auth_token
        )
        self.model.save()

        self.parent = None

        # Model attributes
        self.attributes = ["user_id", "email", "password",
                           "is_admin", "first_name", "last_name",
                           "created_at", "updated_at", "auth_token"]
        self.model_update_index = 4
        self.model_update_input = "Vinai"

    def test_user_authenticate(self):
        # Hash password
        self.model.hash_password()

        with self.assertRaises(Exception) as incorrectPassword:
            User.authenticate("ryan.dens@contrastsecurity.com", "1234")
        self.assertTrue("Incorrect Password!" in incorrectPassword.exception)

        # User should not be found in database
        with self.assertRaises(Exception) as userDNE:
            User.authenticate("ryand.ens@contrastsecurity.com", "12345")
        self.assertTrue("User does not exist!" in userDNE.exception)

        # Correct email with corresponding password
        self.assertEqual(self.model.pk,
                         User.authenticate("ryan.dens@contrastsecurity.com",
                                           "12345").pk)

    def test_build_benefits_data(self):
        self.assertIsNone(Retirement.objects.filter(user_id=self.model).first(), "Benefit already in database")
        self.assertIsNone(PaidTimeOff.objects.filter(user_id=self.model).first(), "Benefit already in database")
        self.assertIsNone(Schedule.objects.filter(user_id=self.model).first(), "Benefit already in database")
        self.assertIsNone(WorkInfo.objects.filter(user_id=self.model).first(), "Benefit already in database")
        self.assertIsNone(Performance.objects.filter(user_id=self.model).first(), "Benefit already in database")

        self.model.build_benefits_data()
        self.assertEqual(Retirement.objects.filter(user_id=self.model).first().user_id,
                         self.model, "Benefit not in database")
        self.assertEqual(PaidTimeOff.objects.filter(user_id=self.model).first().user_id,
                         self.model, "Benefit not in database")
        self.assertEqual(Schedule.objects.filter(user_id=self.model).first().user_id,
                         self.model, "Benefit not in database")
        self.assertEqual(WorkInfo.objects.filter(user_id=self.model).first().user_id,
                         self.model, "Benefit not in database")
        self.assertEqual(Performance.objects.filter(user_id=self.model).first().user_id,
                         self.model, "Benefit not in database")
        user = User.objects.order_by("-user_id").first()

    def test_assign_user_id(self):
        self.model.assign_user_id()
        self.assertEqual(2, self.model.user_id)

    def test_hash_password(self):
        self.assertEqual(self.model.password, "12345")
        self.model.hash_password()
        # Calculated using https://www.freeformatter.com/message-digest.html
        known_md5_output = "827ccb0eea8a706c4c34a16891f84e7b"
        self.assertEqual(known_md5_output, self.model.password)

    def test_generate_token(self):
        self.model.generate_token()
        # Calculated using https://www.freeformatter.com/message-digest.html
        known_md5_output = "c44d3353bc7bc459402506378394ae10"
        self.assertEqual(self.model.auth_token, known_md5_output)

    def test_full_name(self):
        user = User.objects.get(user_id=1)
        self.assertEqual(user.full_name(), "Ryan Dens")
