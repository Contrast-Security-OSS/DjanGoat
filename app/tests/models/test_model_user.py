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
        for user in User.objects.all():
            print(str(user) + "id: " + str(user.user_id) + "\n")
        # Path to file of model
        self.path = "app/models/User/user.py"
        # Create the user
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        self.parent = None

        # Model attributes
        self.attributes = ["user_id", "email", "password",
                           "is_admin", "first_name", "last_name",
                           "created_at", "updated_at", "auth_token"]
        self.model_update_index = 4
        self.model_update_input = "Vinai"

    def test_user_authenticate(self):
        with self.assertRaises(Exception) as incorrectPassword:
            User.authenticate("ryan.dens@example.com", "1234")
        self.assertTrue("Incorrect Password!" in incorrectPassword.exception)

        # User should not be found in database
        with self.assertRaises(User.DoesNotExist):
            User.authenticate("ryand.ens@example.com", "12345")

        # Correct email with corresponding password
        self.assertEqual(self.model.pk,
                         User.authenticate("ryan.dens@example.com",
                                           "12345").pk)

    def test_build_benefits_data(self):
        self.assertIsNone(Retirement.objects.filter(user=self.model).first(), "Benefit already in database")
        self.assertIsNone(PaidTimeOff.objects.filter(user=self.model).first(), "Benefit already in database")
        self.assertIsNone(Schedule.objects.filter(user=self.model).first(), "Benefit already in database")
        self.assertIsNone(WorkInfo.objects.filter(user=self.model).first(), "Benefit already in database")
        self.assertIsNone(Performance.objects.filter(user=self.model).first(), "Benefit already in database")

        self.model.build_benefits_data()
        self.assertEqual(Retirement.objects.filter(user=self.model).first().user,
                         self.model, "Benefit not in database")
        self.assertEqual(PaidTimeOff.objects.filter(user=self.model).first().user,
                         self.model, "Benefit not in database")
        self.assertEqual(Schedule.objects.filter(user=self.model).first().user,
                         self.model, "Benefit not in database")
        self.assertEqual(WorkInfo.objects.filter(user=self.model).first().user,
                         self.model, "Benefit not in database")
        self.assertEqual(Performance.objects.filter(user=self.model).first().user,
                         self.model, "Benefit not in database")
        User.objects.order_by("-user_id").first()

    def test_user_signals_assign_id(self):
        # User is the only user in the db, so its id should be 1
        self.assertEqual(1, self.model.user_id)

    def test_user_signals_generate_token(self):
        """
        Checks that the token generated is correct
        calculated using https://www.freeformatter.com/message-digest.html
        :return:
        """
        old_token = self.model.auth_token
        self.model.generate_token()
        self.model.save()
        self.assertNotEqual(self.model.auth_token, old_token)

    def test_user_signals_hash_password(self):
        # Calculated using https://www.freeformatter.com/message-digest.html
        known_md5_output = "827ccb0eea8a706c4c34a16891f84e7b"
        self.assertEqual(known_md5_output, self.model.password)

    def test_full_name(self):
        user = User.objects.get(user_id=self.model.user_id)
        self.assertEqual(user.full_name(), "Ryan Dens")
