# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.utils import timezone
from django.http import SimpleCookie
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from app.models import Pay, KeyManagement
import app.views as views
from Crypto import Random
import binascii


pay = views.user_messages_pay


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/users/pay/'


class UserPayIndexRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
    Tests checking that that '/users/:user_id/pay' properly handles HttpRequests and routing
    Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
    Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pay_index'
        self.route = '/users/55/pay'
        self.view = pay.user_pay_index
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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Ryan Dens Pay Summary'
        AuthRouteTestingWithKwargs.__init__(self)


class UserPayUpdateDDInfo(TestCase, AuthRouteTestingWithKwargs):
    """
        Tests checking that that '/users/:user_id/pay/update_dd_info' properly handles HttpRequests and routing
        Accepts  POST requests and refuses all others with an error code 405 (Method not allowed)
        Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:update_dd_info'
        self.route = '/users/55/pay/update_dd_info'
        self.view = pay.update_dd_info
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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Update dd info for user 55'
        AuthRouteTestingWithKwargs.__init__(self)

        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = timezone.now()
        km_input_update_date = timezone.now()

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.mixin_model,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        self.client.cookies = SimpleCookie({'auth_token': self.mixin_model.auth_token})

    # Override
    def test_route_exists(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_route_post(self):
        form_args = {"bankAccNumInput": "12345", "bankRouteNumInput": "54321", "percentDepositInput": 20}
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs), form_args, follow=True)
        self.assertEqual(response.status_code, self.responses['POST'])
        pay_objects = Pay.objects.filter(user=self.mixin_model)
        was_pay_added = False
        pay_object = None
        for pay in pay_objects:
            if pay.decrypt_bank_num() == "12345":
                was_pay_added = True
                pay_object = pay

        self.assertTrue(was_pay_added)
        self.assertContains(response, pay_object.bank_account_num)


class UserPayDecryptBankInfo(TestCase, AuthRouteTestingWithKwargs):
    """
        Tests checking that that '/users/:user_id/pay/update_dd_info' properly handles HttpRequests and routing
        Accepts  POST requests and refuses all others with an error code 405 (Method not allowed)
        Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:decrypt_bank_acct_num'
        self.route = '/users/55/pay/decrypt_bank_acct_num'
        self.view = pay.decrypt_bank_acct_num
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
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'Decrypt the bank info 55'
        AuthRouteTestingWithKwargs.__init__(self)

        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = timezone.now()
        km_input_update_date = timezone.now()

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.mixin_model,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        self.client.cookies = SimpleCookie({'auth_token': self.mixin_model.auth_token})

    # Override
    def test_route_exists(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_route_post(self):
        pay = Pay.objects.create(user=self.mixin_model,
                                 bank_account_num="12345",
                                 bank_routing_num="54321",
                                 percent_of_deposit=20,
                                 created_at=timezone.now(),
                                 updated_at=timezone.now())

        form_args = {"account_number": pay.bank_account_num}
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs), form_args, follow=True)
        self.assertEqual(response.status_code, self.responses['POST'])
        self.assertEqual(response.content, "12345")


class UserShowPayRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
       Tests checking that that '/users/:user_id/pay/id/' properly handles HttpRequests and routing
       Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
       Tested on user_id 55 and id 22
     """

    def setUp(self):
        AuthRouteTestingWithKwargs.__init__(self)
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pay_user'
        self.route = '/users/55/pay/22'
        self.view = pay.user_pay
        self.responses = {
            'exists': 200,
            'GET': 405,
            'POST': 405,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 200,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        input_iv = binascii.hexlify(Random.new().read(8))
        km_input_create_date = timezone.now()
        km_input_update_date = timezone.now()

        self.key_model = KeyManagement.objects.create(
            iv=input_iv, user=self.mixin_model,
            created_at=km_input_create_date,
            updated_at=km_input_update_date
        )

        self.pay = Pay.objects.create(bank_account_num="1234",
                                      bank_routing_num="5678",
                                      percent_of_deposit=10,
                                      user=self.mixin_model,
                                      created_at=timezone.now(),
                                      updated_at=timezone.now())
        self.kwargs = {'user_id': 55, 'pay_id': self.pay.id}
        self.expected_response_content = 'Success!'

    def test_route_exists(self):
        response = self.client.delete(reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])
        self.assertContains(response, AuthRouteTestingWithKwargs.not_logged_in_message)
