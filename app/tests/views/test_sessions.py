from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
from app.models.User.user import User
import pytz
import datetime
import app.views as views

sessions = views.sessions_views


class TestLogin(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:login'
        self.route = '/login'
        self.view = sessions.login
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class TestLogout(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:logout'
        self.route = '/logout'
        self.view = sessions.login
        self.responses = {
            'exists': 302,
            'GET': 200,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class SessionsIndexTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:sessions_index'
        self.route = '/sessions'
        self.view = sessions.sessions_index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}

    def test_route_post(self):

        # Create user in database
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        factory_request = self.factory.post('/sessions/')
        factory_response = sessions.sessions_index(factory_request, email="ryan.dens@example.com", password="12345", path="/dashboard")
        self.assertEqual(factory_response.status_code, 302)

        client_request = self.client.post('/sessions/', {'email': 'ryan.dens@example.com', 'password': '12345',
                                                         'path': '/dashboard/home'}, follow=True)
        self.assertEqual(client_request.status_code, 200)
        self.assertTrue("Current Statistics" in client_request.content)
