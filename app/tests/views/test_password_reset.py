# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from django.shortcuts import reverse
from app.tests.mixins import RouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from app.models import User
import app.views as views
import pytz
import datetime
import hashlib
import pickle
import base64

password_reset = views.password_reset_views


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/password_resets/'


class ForgotPassword(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:forgot_password'
        self.route = '/forgot_password'
        self.view = password_reset.forgot_password
        self.responses = {
            'exists': 405,
            'GET': 405,
            'POST': 302,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}


class ConfirmTokens(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:password_resets'
        self.route = '/password_resets'
        self.view = password_reset.confirm_token
        self.responses = {
            'exists': 302,
            'GET': 302,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}
        self.user = User.objects.create(first_name="vinai",
                                        last_name="rachakonda",
                                        email='hello@email.com',
                                        password="password",
                                        is_admin=True,
                                        created_at=pytz.utc.localize(
                                            datetime.datetime(2017, 6, 1, 0,
                                                              0)),
                                        updated_at=pytz.utc.localize(
                                            datetime.datetime(2017, 6, 1, 0,
                                                              0)))

    def test_valid_token_returns_reset_form(self):
        response = self.client.get(reverse(
            'app:password_resets') + '?token=1-cb440f309ad5be39a03b7e7c0ba9d4d6')
        self.assertContains(response, 'Forgot Password', status_code=200)

    def test_invalid_token_redirects_to_login(self):
        response = self.client.get(reverse(
            'app:password_resets') + '?token=1-cb440f309ad5be39a03b7e7c0bd4d6')
        self.assertEquals(302, response.status_code)


class ResetPassword(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:password_resets'
        self.route = '/password_resets'
        self.view = password_reset.reset_password
        self.responses = {
            'exists': 302,
            'GET': 405,
            'POST': 302,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {}
        self.user = User.objects.create(first_name="resetP",
                                        last_name="rachakonda",
                                        email='hello@email.com',
                                        password="password",
                                        is_admin=True,
                                        created_at=pytz.utc.localize(
                                            datetime.datetime(2017, 6, 1, 0,
                                                              0)),
                                        updated_at=pytz.utc.localize(
                                            datetime.datetime(2017, 6, 1, 0,
                                                              0)))

    def test_password_is_updated(self):
        encoded = base64.b64encode(
            pickle.dumps(User.objects.get(first_name="resetP")))
        data = {'password': '123456',
                'password_confirmation': '123456',
                'user': encoded}
        self.client.get(reverse(
            'app:password_resets') + '?token=1-cb440f309ad5be39a03b7e7c0ba9d4d6')

        self.client.post(reverse(
            'app:password_resets'), data=data)
        hashed_password = hashlib.md5('123456'.encode()).hexdigest()

        self.assertEquals(hashed_password,
                          User.objects.get(first_name="resetP").password)
