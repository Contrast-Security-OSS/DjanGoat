# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from django.urls import reverse
import app.views as views

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
        self.expected_response_content = 'Pay index for user 55'
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


class UserNewPayRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
        Tests checking that that '/users/:user_id/user/new' properly handles HttpRequests and routing
        Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
        Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pay_new'
        self.route = '/users/55/pay/new'
        self.view = pay.new_user_pay
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
        self.expected_response_content = 'New pay for 55'
        AuthRouteTestingWithKwargs.__init__(self)


class UserEditPayRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
    Tests checking that that '/users/:user_id/pay/id/edit' properly handles HttpRequests and routing
    Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
    Tested on user_id 55 and id 22
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pay_edit'
        self.route = 'users/55/pay/22/edit'
        self.view = pay.edit_user_pay
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
        self.kwargs = {'user_id': 55, 'id': 22}
        self.expected_response_content = 'Edit pay for user 55 for pay with id 22'
        AuthRouteTestingWithKwargs.__init__(self)


class UserShowRetirementRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
       Tests checking that that '/users/:user_id/pay/id/' properly handles HttpRequests and routing
       Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
       Tested on user_id 55 and id 22
     """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pay_user'
        self.route = '/users/55/pay/22'
        self.view = pay.user_pay
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
        self.kwargs = {'user_id': 55, 'id': 22}
        self.expected_response_content = 'Pay for user 55 for pay with id 22'
        AuthRouteTestingWithKwargs.__init__(self)
