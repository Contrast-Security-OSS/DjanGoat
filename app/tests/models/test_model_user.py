# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.tests.mixins import Pep8ModelTests


class UserModelTests(TestCase, Pep8ModelTests):
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

        self.input_email = "ryan.dens@contrastsecurity.com"
        self.input_password = "12345"
        self.input_admin = True
        self.input_first_name = "Ryan"
        self.input_last_name = "Dens"
        self.input_create_date = datetime.datetime(2017, 6, 1, 0, 0)
        self.input_create_date = pytz.utc.localize(self.input_create_date)
        self.input_update_date = datetime.datetime(2017, 6, 3, 0, 0)
        self.input_update_date = pytz.utc.localize(self.input_update_date)
        self.input_auth_token = "test"
        self.user = User.objects.create(
            user_id=1,
            email=self.input_email, password=self.input_password,
            is_admin=self.input_admin, first_name=self.input_first_name,
            last_name=self.input_last_name, created_at=self.input_create_date,
            updated_at=self.input_update_date, auth_token=self.input_auth_token)
        self.user.save()
        self.db_user = User.objects.filter(user_id=1).first()

    def test_create_user(self):
        self.assertNotEqual(self.db_user, None)

    def test_read_user(self):
        self.assertEqual(self.db_user, self.user)

    def test_update_user(self):
        self.user.first_name = "Vinai"
        self.user.save()
        self.db_user = User.objects.filter(user_id=1).first()
        self.assertEqual(self.user.first_name, self.db_user.first_name)

    def test_delete_user(self):
        response = self.user.delete()
        num_objects_deleted = response[0]
        '''1 object deleted from database'''
        self.assertEqual(num_objects_deleted, 1)

        self.db_user = User.objects.filter(user_id=1).first()
        '''User with user_id=1 no longer in database'''
        self.assertEqual(self.db_user, None)
