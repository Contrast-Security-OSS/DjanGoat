# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
from django.utils import timezone
from app.models import User


class UserModelTests(TestCase):

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
        self.input_email = "ryan.dens@contrastsecurity.com"
        self.input_password = "12345"
        self.input_admin = True
        self.input_first_name = "Ryan"
        self.input_last_name = "Dens"
        self.input_create_date = datetime.date(2017, 6, 1)
        self.input_update_date = datetime.date(2017, 6, 3)
        self.input_auth_token = "test"
        self.user = User.objects.create(
            email=self.input_email, password=self.input_password,
            is_admin=self.input_admin, first_name=self.input_first_name,
            last_name=self.input_last_name, created_at=self.input_create_date,
            updated_at=self.input_update_date, auth_token=self.input_auth_token)
        self.user.save()

    def test_create_user(self):
        self.assertNotEqual(self.user, None)

    def test_read_user(self):
        self.assertEqual(self.user.email, self.input_email)
        self.assertEqual(self.user.password, self.input_password)
        self.assertEqual(self.user.is_admin, self.input_admin)
        self.assertEqual(self.user.first_name, self.input_first_name)
        self.assertEqual(self.user.last_name, self.input_last_name)
        self.assertEqual(self.user.created_at, self.input_create_date)
        self.assertEqual(self.user.updated_at, self.input_update_date)
        self.assertEqual(self.user.auth_token, self.input_auth_token)

    def test_update_user(self):
        # self.user.first_name = "Better Ryan"
        # self.user.last_name = "Dens2"
        # self.user.is_admin = False
        # self.user.email = "ryan.dens2@contrastsecurity.com"
        # self.user.password = "12345"
        # self.user.created_at = datetime.date(2017, 6, 4)
        # self.user.updated_at = datetime.date(2017, 6, 8)
        # self.user.auth_token = "test2"
        # self.user.save()
        # self.assertEqual(self.user.email, "ryan.dens2@contrastsecurity.com")
        # self.assertEqual(self.user.password, "12345")
        # self.assertEqual(self.user.is_admin, False)
        # self.assertEqual(self.user.first_name, "Better Ryan")
        # self.assertEqual(self.user.last_name, "Dens2")
        # self.assertEqual(self.user.created_at, datetime.date(2017, 6, 4))
        # self.assertEqual(self.user.updated_at, datetime.date(2017, 6, 8))
        # self.assertEqual(self.user.auth_token, "test2")
        obj = User.objects.filter(first_name="Ryan")
        print(obj.first())

    def test_delete_user(self):
        response = self.user.delete()
        # self.assertEqual()
