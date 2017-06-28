from __future__ import unicode_literals

import datetime

import pytz
from django.test import TestCase, RequestFactory, Client

import app.views.api.users.views as api_users_views
from app.models import User
from app.tests.mixins import AuthRouteTestingWithKwargs


class TestApiMobileIndex(TestCase):
    def setUp(self):
        self.client = Client()
        input_email = "cat.dog@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Cat"
        input_last_name = "Dog"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )
        input_email = "bird.cow@contrastsecurity.com"
        input_password = "54321"
        input_admin = True
        input_first_name = "Bird"
        input_last_name = "Cow"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    def test_response_content(self):
        response = self.client.get('/api/v1/mobile/?class=User')
        self.assertIn('827ccb0eea8a706c4c34a16891f84e7b', response.content)
        self.assertIn('01cfcd4f6b8770febfb40cb906715822', response.content)


class TestApiMobileId(TestCase):
    def setUp(self):
        self.client = Client()
        input_email = "cat.dog@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Cat"
        input_last_name = "Dog"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )
        input_email = "bird.cow@contrastsecurity.com"
        input_password = "54321"
        input_admin = True
        input_first_name = "Bird"
        input_last_name = "Cow"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    def test_response_content(self):
        response = self.client.get('/api/v1/mobile/' + str(self.model.id) + '?class=User')
        self.assertNotIn('827ccb0eea8a706c4c34a16891f84e7b', response.content)
        self.assertIn('01cfcd4f6b8770febfb40cb906715822', response.content)


class ApiUsersIndexTest(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_index'
        self.route = '/api/v1/users'
        self.view = api_users_views.api_index
        self.responses = {
            'exists': 401,
            'GET': 401,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class ApiUsersByIDTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:api_users_id'
        self.route = '/api/v1/users/5'
        self.view = api_users_views.api
        self.responses = {
            'exists': 401,
            'GET': 401,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'id_number': 5}
