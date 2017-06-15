# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from django_webtest import WebTest
import app.views as views

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
class UserEditRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
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


# Tests checking that that '/users/:id/account_settings' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserAccountSettingsRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
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


# Tests checking that that '/users/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserViewRoutingAndHttpTests(TestCase, RouteTestingWithKwargs):
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


class UserViewSignUpUserFormTests(TestCase):

    def setUp(self):
        pass

class UserViewsSignUpUserFormTests(WebTest):

    def test_view_page(self):
        page = self.app.get('/signup/')
        print(page.forms)


class UserViewSignUpUserLogicTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.param = {'email': 'ziyang@contrast.com', 'first_name': 'ziyang',
                      'last_name': 'wang', 'password': '123456',
                      'confirm': '123456'}

    def test_redirect_on_form_submit(self):
        """
        response_signup = self.client.get('/signup/')
        form = response_signup.context
        self.assertIsNotNone(form)
        print(form)
        data = form.initial()
        print(data)
        """

    def test_redirct_on_signup_fail(self):
        pass

    def test_redirect_on_signup_success(self):
        pass

    def test_invalid_password_length(self):
        pass

    def test_not_matched_password_confirm(self):
        pass

    def test_bad_email_format(self):
        pass

    def test_email_already_exist(self):
        pass

    def test_error_sql_create_user(self):
        pass

    def test_login_on_signup_success(self):
        pass
