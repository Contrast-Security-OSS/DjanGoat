# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import KeyManagement


class UserModelTests(TestCase):

    user = None
    input_email = None
    input_password = None
    input_admin = None
    input_first_name = None
    input_last_name = None
    u_input_create_date = None
    u_input_update_date = None
    input_auth_token = None

    def setUp(self):
        self.input_user_id = 1
        self.input_email = "ryan.dens@contrastsecurity.com"
        self.input_password = "12345"
        self.input_admin = True
        self.input_first_name = "Ryan"
        self.input_last_name = "Dens"
        self.u_input_create_date = datetime.datetime(2017, 6, 1, 0, 0)
        self.u_input_create_date = pytz.utc.localize(self.u_input_create_date)
        self.u_input_update_date = datetime.datetime(2017, 6, 3, 0, 0)
        self.u_input_update_date = pytz.utc.localize(self.u_input_update_date)
        self.input_auth_token = "test"
        self.user = User.objects.create(
            user_id=self.input_user_id,
            email=self.input_email, password=self.input_password,
            is_admin=self.input_admin, first_name=self.input_first_name,
            last_name=self.input_last_name, created_at=self.u_input_create_date,
            updated_at=self.u_input_update_date, auth_token=self.input_auth_token
        )
        self.user.save()

        #Create KeyManagement Model
        self.input_iv = "my_iv"
        self.km_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        self.km_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.key_management = KeyManagement.objects.create(
            iv=self.input_iv, user_id = self.user,
            created_at=self.km_input_create_date,
            updated_at=self.km_input_update_date
        )
        self.key_management.save()
        self.db_key_management = KeyManagement.objects.filter(iv=self.input_iv).first()

    def test_create_key_management(self):
        self.assertNotEqual(self.db_key_management, None)

    def test_read_key_management(self):
        self.assertEqual(self.db_key_management, self.key_management)

    def test_update_key_management(self):
        self.key_management.iv = "my_iv2"
        self.key_management.save()
        self.db_key_management = KeyManagement.objects.filter(pk=self.key_management.pk).first()
        self.assertEqual(self.key_management.iv, self.db_key_management.iv)

    def test_delete_key_management(self):
        response = self.key_management.delete()
        num_objects_deleted = response[0]
        '''1 object deleted from database'''
        self.assertEqual(num_objects_deleted, 1)

        self.db_key_management = KeyManagement.objects.filter(pk=self.key_management.pk).first()
        '''Key management with primary key matching the deleted key management's primary key no longer in database'''
        self.assertEqual(self.db_key_management, None)

    def test_delete_user_and_key_management(self):
        """Test to ensure key management is deleted when its user is deleted.
        """
        response = self.user.delete()
        num_objects_deleted = response[0]
        '''2 objects deleted from database'''
        self.assertEqual(num_objects_deleted, 2)

        self.db_key_management = KeyManagement.objects.filter(pk=self.key_management.pk).first()
        db_user = User.objects.filter(pk=self.user.pk).first()
        self.assertIsNone(self.db_key_management, "Key Management not deleted from database")
        self.assertIsNone(db_user, "User not deleted from the database")


