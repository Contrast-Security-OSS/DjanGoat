# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from django_webtest import WebTest
from django.urls import reverse
import app.views as views
from app.models import Pay, KeyManagement
from django.utils import timezone
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

    # Override
    def test_route_exists(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_route_post(self):
        self.param = {'email': 'ziyang@contrast.com', 'first_name': 'ziyang',
                      'last_name': 'wang', 'password': '123456',
                      'confirm': '123456'}
        # page = self.app.get('/users/55/pays')
        # self.assertEqual(len(page.forms), 2)
        # form = page.forms[0]
        # form.set('email', self.param['email'])


class UserPayDecryptBankInfo(TestCase, AuthRouteTestingWithKwargs):
    """
        Tests checking that that '/users/:user_id/pay/update_dd_info' properly handles HttpRequests and routing
        Accepts  POST requests and refuses all others with an error code 405 (Method not allowed)
        Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:decrypted_bank_acct_num'
        self.route = '/users/55/pay/decrypted_bank_acct_num'
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

    # Override
    def test_route_exists(self):
        response = self.client.post(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])


class UserShowRetirementRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
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
        self.kwargs = {'user_id': 55, 'id': self.pay.id}
        self.expected_response_content = 'Success!'

    def test_route_exists(self):
        response = self.client.delete(reverse(self.route_name, kwargs=self.kwargs))
        self.assertEqual(response.status_code, self.responses['exists'])
