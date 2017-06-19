from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

import pytz
import datetime
from django.urls import reverse
from app.models import User
import json


class TestSensitiveDataExposure(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.kwargs = {'id_number': 1}
        input_email = "vinai.dens@contrastsecurity.com"
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
