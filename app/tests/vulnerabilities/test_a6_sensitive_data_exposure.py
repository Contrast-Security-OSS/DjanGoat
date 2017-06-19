from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

import app.views.api.mobile.views as api_mobile_views
import app.views.api.users.views as api_users_views
import pytz
import datetime
from app.tests.mixins import RouteTestingWithKwargs
from django.urls import reverse
from app.models import User
import json


class TestSensitiveDataExposure(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.kwargs = {'id_number': 1}

    def test_password_is_revealed(self):
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
        user = User.objects.get(first_name="Vinai!")
        self.kwargs = {'id_number': user.user_id}
        response = self.client.get(reverse(self.route_name, kwargs=self.kwargs))
        content = json.loads(response.content)[0]['fields']
        self.assertTrue('password' in content)