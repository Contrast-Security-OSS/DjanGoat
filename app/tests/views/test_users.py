# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.Mixins import RouteTestingMixin

import app.views as views

users = views.users_views


# Tests checking that that '/users' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class UsersIndexRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_index'
        self.route = '/users'
        self.view = users.index
        self.responses = [200, 200, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/users/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class UsersNewRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_new'
        self.route = '/users/new'
        self.view = users.new_user
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/signup' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class UserSignupRoutingAndHttpTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_signup'
        self.route = '/signup'
        self.view = users.signup
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/users/:id/edit' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserEditRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the /users/55/edit
    # and ensuring the response code is 200 (OK)
    def test_user_edit_route_exists(self):
        response = self.client.get(reverse('app:user_edit', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_user_edit_get(self):
        request = self.factory.get('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_edit_post(self):
        request = self.factory.post('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_put(self):
        request = self.factory.put('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_delete(self):
        request = self.factory.delete('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_head(self):
        request = self.factory.head('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_options(self):
        request = self.factory.options('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_trace(self):
        request = self.factory.trace('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_edit_patch(self):
        request = self.factory.patch('/users/55/edit')
        response = users.edit_user(request, 55)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/users/:id/account_settings' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserAccountSettingsRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the /users/55/account_settings
    # and ensuring the response code is 200 (OK)
    def test_user_account_settings_route_exists(self):
        response = self.client.get(reverse('app:user_account_settings', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_user_account_settings_get(self):
        request = self.factory.get('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_account_settings_post(self):
        request = self.factory.post('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_put(self):
        request = self.factory.put('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_delete(self):
        request = self.factory.delete('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_head(self):
        request = self.factory.head('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_options(self):
        request = self.factory.options('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_trace(self):
        request = self.factory.trace('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_account_settings_patch(self):
        request = self.factory.patch('/users/55/account_settings')
        response = users.account_settings(request, 55)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/users/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserViewRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/
    # and ensuring the response code is 200 (OK)
    def test_users_view_route_exists(self):
        response = self.client.get(reverse('app:user_view', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_users_view_get(self):
        request = self.factory.get('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_users_view_post(self):
        request = self.factory.post('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_users_view_put(self):
        request = self.factory.put('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_users_view_delete(self):
        request = self.factory.delete('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_users_view_head(self):
        request = self.factory.head('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_users_view_options(self):
        request = self.factory.options('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_users_view_trace(self):
        request = self.factory.trace('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_users_view_patch(self):
        request = self.factory.patch('/users/55')
        response = users.user_view(request, 55)
        self.assertEqual(response.status_code, 200)
