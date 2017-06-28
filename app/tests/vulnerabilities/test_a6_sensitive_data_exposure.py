from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.http import SimpleCookie
from app.models import User, WorkInfo, KeyManagement
from Crypto import Random
import pytz
import datetime
import json
import binascii


class SensitiveDataExposureApiTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.kwargs = {'id_number': 1}
        input_email = "vinai.dens@example.com"
        input_password = "wopeqop"
        input_admin = True
        input_first_name = "Vinai!"
        input_last_name = "Rachakonda"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )
        self.model = User.objects.create(
            email="ryan.rachakonda@example.com", password=input_password,
            is_admin=input_admin, first_name='ryan',
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    def test_password_is_revealed(self):
        user = User.objects.get(first_name="Vinai!")
        self.kwargs = {'id_number': user.user_id}
        request = reverse(self.route_name, kwargs=self.kwargs)
        response = self.client.get(request,
                                   **{'HTTP_AUTHORIZATION': 'Token token=1-01de24d75cffaa66db205278d1cf900bf087a737'})
        content = json.loads(response.content)[0]['fields']
        self.assertTrue('password' in content)

    def test_401_with_invalid_token(self):
        user = User.objects.get(first_name="Vinai!")
        self.kwargs = {'id_number': user.user_id}
        request = reverse(self.route_name, kwargs=self.kwargs)
        response = self.client.get(request,
                                   **{'HTTP_AUTHORIZATION': 'Token token=1-fjfsasdja03'})
        self.assertEquals(401, response.status_code)

    def test_non_admin_gets_id_response(self):
        self.kwargs = {'id_number': 5}
        user = User.objects.get(first_name="Vinai!")
        user.is_admin = False
        user.save()
        request = reverse(self.route_name, kwargs=self.kwargs)
        response = self.client.get(request,
                                   **{'HTTP_AUTHORIZATION': 'Token token=1-01de24d75cffaa66db205278d1cf900bf087a737'})
        content = json.loads(response.content)[0]['fields']
        self.assertEquals('vinai.dens@example.com', content['email'])

    def test_new_line_gives_too_much_info(self):
        route_name = 'app:api_users_index'
        kwargs = {}
        request = reverse(route_name, kwargs=kwargs)
        response = self.client.get(request,
                                   **{'HTTP_AUTHORIZATION': 'Token token=1%0A2-050ddd40584978fe9e82840b8b95abb98e4786dc'})
        content = json.loads(response.content)
        self.assertTrue(len(content) > 1)

    def test_new_line_token_allows_you_to_act_like_another_user(self):
        self.kwargs = {'id_number': 2}
        user = User.objects.get(first_name="Vinai!")
        user.is_admin = False
        user.save()
        request = reverse(self.route_name, kwargs=self.kwargs)
        response = self.client.get(request,
                                   **{'HTTP_AUTHORIZATION': 'Token token=1%0A2-050ddd40584978fe9e82840b8b95abb98e4786dc'})
        content = json.loads(response.content)[0]['fields']
        self.assertEquals('vinai.dens@example.com', content['email'])

class SensitiveDataExposureSSNTest(TestCase):
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

        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 4, 0, 0))
        km_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 5, 0, 0))

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.user,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        self.client = Client()
        self.client.cookies = SimpleCookie({'auth_token': self.user.auth_token})

    def test_full_unencrypted_ssn_in_response(self):
        response = self.client.get(self.route, follow=True)
        self.assertEqual(response.context['work_info'].SSN, "111-22-3333")

    def test_ssn_stored_unencrypted(self):
        self.assertEqual(WorkInfo.objects.get(user=self.user).SSN, "111-22-3333")

