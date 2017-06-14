# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class UserModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
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
        with self.assertRaises(Exception) as context:
            User.authenticate("ryan.dens@contrastsecurity.com", "1234")
        self.assertTrue("Incorrect Password!" in context.exception)

        # User should not be found in database
        with self.assertRaises(AttributeError):
            User.authenticate("ryand.ens@contrastsecurity.com", "12345")

        self.assertEqual(self.model.pk,
                         User.authenticate("ryan.dens@contrastsecurity.com",
                                           "12345").pk)
