# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from app.views import sessions_views as sessions
from app.views.utils import simulate_simple_authentication
from pygoat.settings import BASE_DIR
import os
import app.views as views

benefit_forms = views.user_benefit_forms_views


class UserBenefitFormsPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/users/benefit_forms/'


# Tests checking that that '/users/:user_id/benefit_forms' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserBenefitFormsRoutingAndHttpTests(TestCase,
                                          AuthRouteTestingWithKwargs):
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
        self.expected_response_content = 'Health Insurance'
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
        self.expected_response_content = 'Upload user benefit form'
        AuthRouteTestingWithKwargs.__init__(self)

    # Override
    # Verifies the route exists by getting the /upload
    # and ensuring the response code is 200 (OK)
    def test_route_exists(self):
        response = self.client.post(reverse('app:upload_benefit_form'),
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_can_send_file(self):
        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path=self.route,
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        with open(BASE_DIR + '/public/docs/Dental_n_Stuff.pdf') as fp:
            response = self.client.post(reverse('app:upload_benefit_form'),
                                        {'myfile': fp, 'backup': False},
                                        follow=True)
            self.assertContains(response, 'File was successfully uploaded!')
            self.assertTrue(
                os.path.isfile(BASE_DIR + '/media/data/Dental_n_Stuff.pdf'))
            os.remove(BASE_DIR + '/media/data/Dental_n_Stuff.pdf')  # cleanup

    def test_no_upload_returns_error_message(self):
        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path=self.route,
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        response = self.client.post(reverse('app:upload_benefit_form'),
                                    {'backup': False}, follow=True)
        self.assertContains(response,
                            'Something went wrong! Are you sure you selected a file?')
        self.assertFalse(
            os.path.isfile(BASE_DIR + '/media/data/Dental_n_Stuff.pdf'))


# Tests checking that that '/download' properly handles HttpRequests and routing
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DownloadBenefitFormsRoutingAndHttpTests(TestCase,
                                              AuthRouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:download_benefit_form'
        self.route = '/download/'
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
        self.expected_response_content = None
        AuthRouteTestingWithKwargs.__init__(self)

    def test_dental_n_stuff_download(self):
        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path=self.route,
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        response = self.client.get(
            reverse(self.route_name) + '/?name=public/docs/Dental_n_Stuff.pdf',
            follow=True)
        self.assertEquals(response['Content-Disposition'],
                          'attachment; filename=%s' \
                          % os.path.basename('public/docs/Dental_n_Stuff.pdf'))

    def test_health_n_stuff_download(self):
        simulate_simple_authentication(factory=self.factory,
                                       client=self.client,
                                       email="ryan.dens@example.com",
                                       password="12345",
                                       path=self.route,
                                       add_messages_middleware=AuthRouteTestingWithKwargs.add_messages_middleware,
                                       views=sessions)

        response = self.client.get(
            reverse(self.route_name) + '/?name=public/docs/Health_n_Stuff.pdf',
            follow=True)
        self.assertEquals(response['Content-Disposition'],
                          'attachment; filename=%s' \
                          % os.path.basename('public/docs/Health_n_Stuff.pdf'))
