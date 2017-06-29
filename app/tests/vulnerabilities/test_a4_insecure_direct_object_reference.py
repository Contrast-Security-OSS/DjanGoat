from __future__ import unicode_literals
from django.test import TestCase, Client
from django.http import SimpleCookie
from app.models import User, WorkInfo
import pytz
import datetime


class InsecureDirectObjectReferenceTest(TestCase):

    def setUp(self):
        # Create User Model
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = False
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))

        self.user = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        self.other_user = User.objects.create(
            email=input_email+"2", password=input_password+"2",
            is_admin=input_admin, first_name=input_first_name+"2",
            last_name=input_last_name+"2", created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        self.route = "/users/" + str(self.user.id) + "/work_info"

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
            user=self.user,
        )

        self.other_model = WorkInfo.objects.create(
            income=input_income+"2",
            bonuses=input_bonuses+"2",
            years_worked=input_years_worked+1,
            SSN="111-22-4444",
            encrypted_ssn=input_encrypted_ssn,
            DoB=input_dob,
            created_at=perf_input_create_date,
            updated_at=perf_input_update_date,
            user=self.other_user
        )

        # authenticate the user
        self.client = Client()
        self.client.cookies = SimpleCookie({'auth_token': self.user.auth_token})

    def test_insecure_direct_object_reference(self):
        """
        Test to make sure insecure direct object reference is present on the workinfo page
        First, authenticated user (self.user) goes to their own workinfo page and makes
        sure their SSN is there and that self.other_user's SSN is not there
        Then, does insecure direct object reference, by changing the url to be the
        other user's id. Then, it checks to see if the other user's SSN is there
        and makes sure their SSN is not there.
        :return:
        """
        self_response = self.client.get(self.route, follow=True)
        self.assertContains(self_response, self.model.SSN)
        self.assertNotContains(self_response, self.other_model.SSN)

        dor_route = "/users/" + str(self.other_user.id) + "/work_info"
        insecure_dor_response = self.client.get(dor_route, follow=True)
        self.assertContains(insecure_dor_response, self.other_model.SSN)
        self.assertNotContains(insecure_dor_response, self.model.SSN)




