# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs, AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from django_webtest import WebTest
from django.utils import timezone
import app.views as views
from app.models import User

users = views.users_views


class UsersPep8Tests(TestCase, Pep8ViewsTests):

    def setUp(self):
        self.path = 'app/views/users/'


# Tests checking that that '/users' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error
# code 405 (Method not allowed)
class UsersIndexRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_index'
        self.route = '/users'
        self.view = users.index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


# Tests checking that that '/users/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405
# (Method not allowed)
class UsersNewRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:users_new'
        self.route = '/users/new'
        self.view = users.new_user
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


# Tests checking that that '/signup' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405
# (Method not allowed)
class UserSignupRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_signup'
        self.route = '/signup'
        self.view = users.signup
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


# Tests checking that that '/users/:id/edit' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserEditRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_edit'
        self.route = '/users/55/edit'
        self.view = users.edit_user
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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Edit user 55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:id/account_settings' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserAccountSettingsRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_account_settings'
        self.route = '/users/55/account_settings'
        self.view = users.account_settings
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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Account settings for user #55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserViewRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_view'
        self.route = '/users/55'
        self.view = users.user_view
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 405,
            'PUT': 200,
            'PATCH': 200,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'User 55'
        AuthRouteTestingWithKwargs.__init__(self)


class UserViewsSignUpUserFormTests(WebTest):

    def setUp(self):
        self.param = {'email': 'ziyang@contrast.com', 'first_name': 'ziyang',
                      'last_name': 'wang', 'password': '123456',
                      'confirm': '123456'}
        page = self.app.get('/signup/')
        self.assertEqual(len(page.forms), 1)
        form = page.forms[0]
        form.set('email', self.param['email'])
        form.set('first_name', self.param['first_name'])
        form.set('last_name', self.param['last_name'])
        form.set('password', self.param['password'])
        form.set('confirm', self.param['confirm'])
        self.form = form

    def test_invalid_password_length_short(self):
        password_short = '12345'
        self.form.set('password', password_short)
        self.form.set('password', password_short)
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        password_short_message = "Password minimum 6 characters"
        self.assertTrue(password_short_message in response_message)
        self.form.set('password', self.param['password'])
        self.form.set('confirm', self.param['confirm'])

    def test_invalid_password_length_long(self):
        password_long = '1'*41
        self.form.set('password', password_long)
        self.form.set('password', password_long)
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        password_long_message = "Password maximum 40 characters"
        self.assertTrue(password_long_message in response_message)
        self.form.set('password', self.param['password'])
        self.form.set('confirm', self.param['confirm'])

    def test_not_matched_password_confirm(self):
        self.form.set('password', '135790')
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        not_matched_message = "Password and Confirm Password does not match"
        self.assertTrue(not_matched_message in response_message)
        self.form.set('password', self.param['password'])

    def test_email_already_exist(self):
        user = User.objects.create(
            email=self.param['email'], password='',
            is_admin=True, first_name='ziyang',
            last_name='wang', created_at=timezone.now(),
            updated_at=timezone.now()
        )
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        email_exist_message = "Email has already been taken"
        self.assertTrue(email_exist_message in response_message)
        user.delete()

    def test_error_sql_create_user(self):
        self.form.set('first_name', 'z'*256)
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        sql_message = "Data too long for column 'first_name'"
        self.assertTrue(sql_message in response_message)
        self.form.set('first_name', self.param['first_name'])

    def test_redirect_and_login_on_signup_success(self):
        response = self.form.submit()
        response_message = response._headers['Set-Cookie']
        user = User.objects.filter(email=self.param['email'])
        self.assertTrue(user)
        auth_token = user.first().auth_token
        self.assertTrue(auth_token in response_message)
        self.assertEqual(response.url, '/dashboard/home')
        user.first().delete()
