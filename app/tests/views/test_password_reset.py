# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

import app.views as views
from app.tests.mixins import RouteTestingMixin

password_reset = views.password_reset_views


class ForgotPassword(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:forgot_password'
        self.route = '/forgot_password'
        self.view = password_reset.forgot_password
        self.responses = [405, 200, 405, 405, 405, 405, 405, 405]

    # override
    def test_route_exists(self):
        response = self.client.get(reverse(self.route_name))
        self.assertEqual(response.status_code, 405)


class PasswordViewHandler(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_password_reset_view_handler_get_request_triggers_confirm_token(self):
        request = self.factory.get('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.content, 'Confirm your token please!')

    def test_password_reset_view_handler_post_request_triggers_reset_password(self):
        request = self.factory.post('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.content, 'Reset your password')

    def test_password_reset_view_handler_post(self):
        request = self.factory.post('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.status_code, 200)

    def test_password_reset_view_handler_put(self):
        request = self.factory.put('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.status_code, 405)

    def test_password_reset_view_handler_delete(self):
        request = self.factory.delete('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.status_code, 405)

    def test_password_reset_view_handler_patch(self):
        request = self.factory.patch('/password_resets')
        response = password_reset.reset_password_handler(request)
        self.assertEqual(response.status_code, 405)


class ConfirmTokens(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:password_resets'
        self.route = '/password_resets'
        self.view = password_reset.confirm_token
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


class ResetPassword(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:password_resets'
        self.route = '/password_resets'
        self.view = password_reset.reset_password
        self.responses = [405, 200, 405, 405, 405, 405, 405, 405]
