# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests


import app.views as views

benefit_forms = views.user_benefit_forms_views


class UserBenefitFormsPep8Tests(TestCase, Pep8ViewsTests):

    def setUp(self):
        self.path = 'app/views/users/benefit_forms/'


# Tests checking that that '/users/:user_id/benefit_forms' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserBenefitFormsRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_benefit_forms'
        self.route = '/users/55/benefit_forms'
        self.view = benefit_forms.user_benefit_forms
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
        self.expected_response_content = 'Benefit forms index55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/benefit_forms/new' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserNewBenefitFormsRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:new_user_benefit_form'
        self.route = '/users/55/benefit_forms/new'
        self.view = benefit_forms.new_user_benefit_form
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
        self.expected_response_content = 'New benefit form55'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/benefit_forms/:benefit_form_id/edit' properly handles HttpRequests and rout-
# ing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and benefit_form_id 22
class UserEditBenefitFormRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:edit_user_benefit_form'
        self.route = '/users/55/benefit_forms/22/edit'
        self.view = benefit_forms.edit_user_benefit_form
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
        self.kwargs = {'user_id': 55, 'benefit_form_id': 22}
        self.expected_response_content = 'edit benefit form5522'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/users/:user_id/benefit_forms/benefit_form_id' properly handles HttpRequests and routing
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on user_id 55 and benefit_form_id 22
class UserShowBenefitFormRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_benefit_form'
        self.route = '/upload'
        self.view = benefit_forms.user_benefit_form
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
        self.kwargs = {'user_id': 55, 'benefit_form_id': 22}
        self.client = Client()
        self.expected_response_content = 'show benefit form5522'
        AuthRouteTestingWithKwargs.__init__(self)


# Tests checking that that '/upload' properly handles HttpRequests and routing
# Accepts POST requests and refuses all others with an error code 405 (Method not allowed)
class UploadRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:upload_benefit_form'
        self.route = '/upload'
        self.view = benefit_forms.upload
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
        self.kwargs = {}
        self.expected_response_content = 'Upload user benefit form'
        AuthRouteTestingWithKwargs.__init__(self)

    # Override
    # Verifies the route exists by getting the /upload
    # and ensuring the response code is 200 (OK)
    def test_route_exists(self):
        response = self.client.post(reverse('app:upload_benefit_form'))
        self.assertEqual(response.status_code, 200)


# Tests checking that that '/download' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DownloadBenefitFormsRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:download_benefit_form'
        self.route = '/download'
        self.view = benefit_forms.download
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
        self.expected_response_content = 'Download user benefit form'
        AuthRouteTestingWithKwargs.__init__(self)
