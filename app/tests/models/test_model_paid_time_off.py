# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import PaidTimeOff


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

        #Create PTO Model
        self.input_sick_days_earned = 20
        self.input_sick_days_taken = 2
        self.input_pto_days_earned = 10
        self.input_pto_days_taken = 4
        self.pto_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        self.pto_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.pto = PaidTimeOff.objects.create(
            sick_days_earned=self.input_sick_days_earned,
            sick_days_taken=self.input_sick_days_taken,
            pto_earned=self.input_pto_days_earned,
            pto_taken=self.input_pto_days_taken,
            created_at=self.pto_input_create_date,
            updated_at=self.pto_input_update_date,
            user_id=self.user
        )

        self.pto.save()
        self.db_pto = PaidTimeOff.objects.filter(pk=self.pto.pk).first()

    def test_create_pto(self):
        self.assertNotEqual(self.db_pto, None)

    def test_read_pto(self):
        self.assertEqual(self.db_pto, self.pto)

    def test_update_pto(self):
        self.pto.sick_days_taken = 5
        self.pto.save()
        self.db_pto = PaidTimeOff.objects.filter(pk=self.pto.pk).first()
        self.assertEqual(self.pto.sick_days_taken, self.db_pto.sick_days_taken)

    def test_delete_pto(self):
        response = self.pto.delete()
        num_objects_deleted = response[0]
        '''1 object deleted from database'''
        self.assertEqual(num_objects_deleted, 1)

        self.db_pto = PaidTimeOff.objects.filter(pk=self.pto.pk).first()
        '''PTO with primary key matching the deleted pto's primary key no longer in database'''
        self.assertEqual(self.db_pto, None)

    def test_delete_user_and_pto(self):
        """Test to ensure pto is deleted when its user is deleted.
        """
        response = self.user.delete()
        num_objects_deleted = response[0]
        '''2 objects deleted from database'''
        self.assertEqual(num_objects_deleted, 2)

        self.db_pto = PaidTimeOff.objects.filter(pk=self.pto.pk).first()
        db_user = User.objects.filter(pk=self.user.pk).first()
        self.assertIsNone(self.db_pto, "PTO not deleted from database")
        self.assertIsNone(db_user, "User not deleted from the database")


