# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

import app.views as views

password_reset = views.password_reset_views


class ForgotPassword(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard index
    # and ensuring the response code is 200 (OK)
    def test_forgot_password_route_exists(self):
        response = self.client.post(reverse('app:forgot_password'))
        self.assertEqual(response.status_code, 200)

    def test_forgot_get(self):
        request = self.factory.get('/forgot_password')
        response = password_reset.forgot_password(request)
        self.assertEqual(response.status_code, 405)

    def test_forgot_post(self):
        request = self.factory.post('/forgot_password')
        response = password_reset.forgot_password(request)
        self.assertEqual(response.status_code, 200)

    def test_forgot_put(self):
        request = self.factory.put('/forgot_password')
        response = password_reset.forgot_password(request)
        self.assertEqual(response.status_code, 405)

    def test_forgot_delete(self):
        request = self.factory.delete('/forgot_password')
        response = password_reset.forgot_password(request)
        self.assertEqual(response.status_code, 405)

    def test_forgot_patch(self):
        request = self.factory.patch('/forgot_password')
        response = password_reset.forgot_password(request)
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


class ConfirmTokens(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard index
    # and ensuring the response code is 200 (OK)
    def test_password_resets_exists(self):
        response = self.client.get(reverse('app:password_resets'))
        self.assertEqual(response.status_code, 200)

    def test_confirm_token_get(self):
        request = self.factory.get('/password_resets')
        response = password_reset.confirm_token(request)
        self.assertEqual(response.status_code, 200)

    def test_confirm_token_post(self):
        request = self.factory.post('/password_resets')
        response = password_reset.confirm_token(request)
        self.assertEqual(response.status_code, 405)

    def test_confirm_token_put(self):
        request = self.factory.put('/password_resets')
        response = password_reset.confirm_token(request)
        self.assertEqual(response.status_code, 405)

    def test_confirm_token_delete(self):
        request = self.factory.delete('/password_resets')
        response = password_reset.confirm_token(request)
        self.assertEqual(response.status_code, 405)

    def test_confirm_token_patch(self):
        request = self.factory.patch('/password_resets')
        response = password_reset.confirm_token(request)
        self.assertEqual(response.status_code, 405)


class ResetPassword(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard index
    # and ensuring the response code is 200 (OK)
    def test_password_resets_exists_post(self):
        response = self.client.post(reverse('app:password_resets'))
        self.assertEqual(response.status_code, 200)

    def test_confirm_token_get(self):
        request = self.factory.get('/password_resets')
        response = password_reset.reset_password(request)
        self.assertEqual(response.status_code, 405)

    def test_reset_password_post(self):
        request = self.factory.post('/password_resets')
        response = password_reset.reset_password(request)
        self.assertEqual(response.status_code, 200)

    def test_reset_password_put(self):
        request = self.factory.put('/password_resets')
        response = password_reset.reset_password(request)
        self.assertEqual(response.status_code, 405)

    def test_reset_password_delete(self):
        request = self.factory.delete('/password_resets')
        response = password_reset.reset_password(request)
        self.assertEqual(response.status_code, 405)

    def test_reset_password_patch(self):
        request = self.factory.patch('/password_resets')
        response = password_reset.reset_password(request)
        self.assertEqual(response.status_code, 405)