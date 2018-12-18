# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.utils import timezone
from django.contrib.messages.storage.fallback import FallbackStorage
from django_webtest import WebTest
from app.tests.mixins import RouteTestingWithKwargs, AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from app.models import User
import app.views as views
import hashlib

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


# Tests checking that that '/users/:id/account_settings' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserAccountSettingsRoutingAndHttpTests(TestCase,
                                             AuthRouteTestingWithKwargs):
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
        self.expected_response_content = 'Update Account Information'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:id' properly handles HttpRequests
# Accepts GET, POST, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
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
            'POST': 200,
            'PUT': 200,
            'PATCH': 405,
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
        self.param = {'email': 'ziyang@example.com', 'first_name': 'ziyang',
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
        self.form.set('confirm', password_short)
        response = self.form.submit()
        self.assertEqual(response.url, '/signup/')
        response_message = response._headers['Set-Cookie']
        password_short_message = "Password minimum 6 characters"
        self.assertTrue(password_short_message in response_message)
        self.form.set('password', self.param['password'])
        self.form.set('confirm', self.param['confirm'])

    def test_invalid_password_length_long(self):
        password_long = '1' * 41
        self.form.set('password', password_long)
        self.form.set('confirm', password_long)
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

    def test_redirect_and_login_on_signup_success(self):
        response = self.form.submit()
        response_message = response._headers['Set-Cookie']
        user = User.objects.filter(email=self.param['email'])
        self.assertTrue(user)
        auth_token = user.first().auth_token
        self.assertTrue(auth_token in response_message)
        self.assertEqual(response.url, '/dashboard/home')
        user.first().delete()


class UserViewsUpdateAccountFormTests(WebTest):
    def setUp(self):
        # First signup and login a user
        self.param = {'email': 'ziyang@example.com', 'first_name': 'ziyang',
                      'last_name': 'wang', 'password': 'ziyangw',
                      'confirm': 'ziyangw'}
        signup_page = self.app.get('/signup/')
        signup_form = signup_page.forms[0]
        signup_form.set('email', self.param['email'])
        signup_form.set('first_name', self.param['first_name'])
        signup_form.set('last_name', self.param['last_name'])
        signup_form.set('password', self.param['password'])
        signup_form.set('confirm', self.param['confirm'])
        form_response = signup_form.submit()
        cookies = form_response._headers['Set-Cookie'].split(';')
        self.cookie = cookies[0].split('=')[1]
        self.user = User.objects.filter(email=self.param['email']).first()
        # Setting up for update account setting test
        self.url = '/users/%s/account_settings' % self.user.id
        update_page = self.app.get(self.url)
        self.assertEqual(len(update_page.forms), 1)
        update_form = update_page.forms[0]
        self.form = update_form
        self.form.set('user_id', self.user.user_id)

    def test_invalid_password_length_short(self):
        password_short = '12345'
        self.form.set('password_new', password_short)
        self.form.set('confirm', password_short)
        response = self.form.submit()
        self.assertEqual(response.url, self.url)
        response_message = response._headers['Set-Cookie']
        password_short_message = "Password minimum 6 characters"
        self.assertTrue(password_short_message in response_message)
        self.form.set('password_new', '')
        self.form.set('confirm', '')

    def test_invalid_password_length_long(self):
        password_long = '1' * 41
        self.form.set('password_new', password_long)
        self.form.set('confirm', password_long)
        response = self.form.submit()
        self.assertEqual(response.url, self.url)
        response_message = response._headers['Set-Cookie']
        password_long_message = "Password maximum 40 characters"
        self.assertTrue(password_long_message in response_message)
        self.form.set('password_new', '')
        self.form.set('confirm', '')

    def test_not_matched_password_confirm(self):
        self.form.set('password_new', '135790')
        self.form.set('confirm', '135780')
        response = self.form.submit()
        self.assertEqual(response.url, self.url)
        response_message = response._headers['Set-Cookie']
        not_matched_message = "Password and Confirm Password does not match"
        self.assertTrue(not_matched_message in response_message)
        self.form.set('password_new', '')
        self.form.set('confirm', '')

    def test_email_already_exist(self):
        user = User.objects.create(
            email="a@b.com", password='',
            is_admin=True, first_name='ziyang',
            last_name='wang', created_at=timezone.now(),
            updated_at=timezone.now()
        )
        self.form.set('email_new', 'a@b.com')
        response = self.form.submit()
        self.assertEqual(response.url, self.url)
        response_message = response._headers['Set-Cookie']
        email_exist_message = "Email has already been taken"
        self.assertTrue(email_exist_message in response_message)
        user.delete()
        self.form.set('email_new', '')

    def test_update_success(self):
        self.assertEqual(self.user.email, self.param['email'])
        self.form.set('email_new', 'zw@example.com')
        response = self.form.submit()
        response_message = response._headers['Set-Cookie']
        updated_user = User.objects.filter(email='zw@example.com').first()
        self.assertTrue(updated_user)
        self.assertEqual(updated_user.email, 'zw@example.com')
        self.assertTrue("Successfully Updated" in response_message)
        self.assertEqual(response.url, self.url)
        self.form.set('email_new', '')

    def test_sql_injection_vulnerability(self):
        # Get a target admin to apply SQL injection
        admin = User.objects.filter(is_admin='1').first()
        admin.password = '1357911'
        admin.save()

        # Send a request by submitting form as a non-admin
        factory = RequestFactory()
        self.form.set('email_new', 'zw@example.com')
        url = "/users/%s" % self.user.user_id
        fields = self.form.submit_fields(None, index=None, submit_value=None)
        request = factory.post(url, dict(fields))
        request.COOKIES['auth_token'] = self.cookie

        # Change fields as SQL injection
        request.POST = request.POST.copy()
        request.POST['password_new'] = '123456'
        request.POST['confirm'] = '123456'
        request.POST['user_id'] = "%s' OR is_admin = '1" % self.user.user_id
        request.path_info = url
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        users.user_view(request, user_id=admin.user_id)

        # Test that admin's password has changed
        new_admin = User.objects.filter(user_id=admin.user_id).first()
        hashed_password = hashlib.md5('123456'.encode()).hexdigest()
        self.assertEqual(new_admin.password, hashed_password)
