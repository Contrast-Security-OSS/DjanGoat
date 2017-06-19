from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
from django.urls import reverse
from app.models import User
import app.views.admin.views as admin_views
import datetime
import pytz


class AdminDashboardTest(TestCase, RouteTestingWithKwargs):
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


class AdminGetUserTest(TestCase, RouteTestingWithKwargs):
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


class AdminDeleteUserTest(TestCase):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_delete_user'
        self.route = '/admin/1/delete_user'
        self.view = admin_views.admin_delete_user
        self.responses = {
            'exists': 200,
            'GET': 405,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'selected_id': 2}
        input_user_id = 2
        input_email = "ryan.dens@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        input_auth_token = "test"

        self.model = User.objects.create(
            user_id=input_user_id,
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date, auth_token=input_auth_token
        )
        self.model.save()

    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_can_delete_a_user(self):
        self.client.post(reverse(self.route_name, kwargs=self.kwargs))  # simulate the post request
        self.assertEquals(0, len(User.objects.all()))

    def test_not_present_user_does_not_do_anything(self):
        self.kwargs = {'selected_id': 5}
        self.client.post(reverse(self.route_name, kwargs=self.kwargs))  # simulate the post request
        self.assertEquals(1, len(User.objects.all()))


class AdminUpdateUserTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_update_user'
        self.route = '/admin/4/update_user'
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
        input_user_id = 1
        input_email = "ryan.dens@contrastsecurity.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Ryan"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        input_auth_token = "test"

        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    # Verifies a route exists
    def test_route_exists(self):
        response = self.client.patch(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_simple_update(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs),
                                    data={'password': 'ds', 'email': 'yo@email.com', 'password_confirmation': 'ds', 'first_name': 'Vinai'})
        self.assertEquals(1, len(User.objects.all()))
        self.assertEquals("yo@email.com", User.objects.get(user_id=1).email)
        self.assertEquals("Vinai", User.objects.get(user_id=1).first_name)


class AdminGetAllUsersTest(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        """ Class for testing admin delete view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:admin_get_all_users'
        self.route = '/admin/5/get_all_users'
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
        self.kwargs = {'selected_id': 5}


class AdminAnalyticsUsersTest(TestCase, RouteTestingWithKwargs):
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
