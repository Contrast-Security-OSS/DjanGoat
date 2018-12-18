import datetime

import pytz
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django_webtest import WebTest

from app.models import User
from app.views import sessions_views as sessions
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.views.utils import simulate_simple_authentication
import app.views.admin.views as admin_views

class AdminDashboardTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin dashboard view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_dashboard'
        self.route = '/admin/5/dashboard'
        self.view = admin_views.admin_dashboard
        self.responses = {
            'exists': 200,
            'GET': 302,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'selected_id': 5}
        self.expected_response_content = 'edit'
        AuthRouteTestingWithKwargs.__init__(self)


class AdminGetUserTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin dashboard view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_get_user'
        self.route = '/admin/5/get_user'
        self.view = admin_views.admin_get_user
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
        self.kwargs = {'selected_id': 5}
        self.expected_response_content = 'fields'
        AuthRouteTestingWithKwargs.__init__(self)


class AdminDeleteUserTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_delete_user'
        self.route = '/admin/1/delete_user'
        self.view = admin_views.admin_delete_user
        self.responses = {
            'exists': 405,
            'GET': 405,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'selected_id': 2}
        self.expected_response_content = "failure"
        AuthRouteTestingWithKwargs.__init__(self)

    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.post(
            reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_can_delete_a_user(self):
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "VINAITEST"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))

        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path='admin/2/delete_user',
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        self.client.delete(reverse(self.route_name,kwargs=self.kwargs))  # simulate the post request
        self.assertEquals(0, len(User.objects.filter(first_name="VINAITEST")))

    def test_not_present_user_does_not_do_anything(self):
        self.kwargs = {'selected_id': 5}

        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path='admin/5/update_user',
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)
        self.client.post(reverse(self.route_name,
                                            kwargs=self.kwargs))  # simulate the post request
        self.assertEquals(1, len(User.objects.all()))


class AdminUpdateUserTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_update_user'
        self.route = '/admin/1/update_user'
        self.view = admin_views.admin_update_user
        self.responses = {
            'exists': 200,
            'GET': 405,
            'POST': 200,
            'PUT': 405,
            'PATCH': 200,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'selected_id': 1}

        self.expected_response_content = "success"
        AuthRouteTestingWithKwargs.__init__(self)

    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.patch(
            reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_simple_update(self):
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "VINAIUPDATETEST"
        input_last_name = "Ryan"
        u_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))

        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path='admin/2/update_user/',
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        self.kwargs = {'selected_id': 2}
        self.client.post(
            reverse(self.route_name, kwargs=self.kwargs),
            data={'password': 'ds', 'email': 'yo@email.com',
                  'password_confirmation': 'ds', 'first_name': 'Vinai'})
        self.assertEquals(2, len(User.objects.all()))
        self.assertEquals("yo@email.com", User.objects.get(user_id=2).email)
        self.assertEquals("Vinai", User.objects.get(user_id=2).first_name)


class AdminGetAllUsersTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_get_all_users'
        self.route = '/admin/1/get_all_users'
        self.view = admin_views.admin_get_all_users
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
        self.kwargs = {'selected_id': 1}
        self.expected_response_content = "First Name"
        AuthRouteTestingWithKwargs.__init__(self)


class AdminAnalyticsUsersTest(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_analytics'
        self.route = '/admin/5/analytics'
        self.view = admin_views.admin_analytics
        self.responses = {
            'exists': 200,
            'GET': 302,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'selected_id': 5}
        self.expected_response_content = 'analytics'
        AuthRouteTestingWithKwargs.__init__(self)


class AdminSQLInjectionInterpolationTest(WebTest):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        User.objects.create(
            email="ryan.dens@example.com", password="12345",
            is_admin=True, first_name="Ryan",
            last_name="Dens",
            created_at=pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0)),
            updated_at=pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        )

    def test_sql_injection_interpolation(self):
        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path='http://127.0.0.1:8000/admin/1/analytics/?ip=127.0.0.1&email=&password%20FROM%20app_user%3B%20select%20user_agent=',
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        # The attack string may vary depending on the system used
        url = 'http://127.0.0.1:8000/admin/1/analytics/?ip=127.0.0.1&email=&email%2C%20password%20FROM%20app_user%3B--'
        response = self.client.get(url)
        self.assertTrue('email' in response.content)
        self.assertTrue('password' in response.content)
