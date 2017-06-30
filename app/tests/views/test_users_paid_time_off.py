# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from django_webtest import WebTest
from app.tests.mixins import AuthRouteTestingWithKwargs
from app.tests.mixins import Pep8ViewsTests
from app.models import User, Schedule
import app.views as views

pto = views.pto_views


class PasswordResetPep8Tests(TestCase, Pep8ViewsTests):
    def setUp(self):
        self.path = 'app/views/users/paid_time_off/'


class UserPTOIndexRoutingAndHttpTests(TestCase, AuthRouteTestingWithKwargs):
    """
    Tests checking that that '/users/:user_id/paid_time_off' properly handles HttpRequests and routing
    Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
    Tested on id #55
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:pto_index'
        self.route = '/users/55/paid_time_off'
        self.view = pto.index
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
        self.expected_response_content = 'PTO Calendar'
        AuthRouteTestingWithKwargs.__init__(self)
        self.mixin_model.build_benefits_data()

    def test_route_post(self):
        if (self.responses['POST'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_post()
        else:
            self.expected_response_content = 'No form found'
            request = self.factory.post(self.route)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)


class UserViewsPTOTests(WebTest):
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
        signup_form.submit()
        self.user = User.objects.filter(email=self.param['email']).first()

        # Setting up PTO form
        self.url = '/users/%s/paid_time_off/' % self.user.user_id
        pto_page = self.app.get(self.url)
        self.assertEqual(len(pto_page.forms), 1)
        self.form = pto_page.forms[0]

    def test_empty_field(self):
        response = self.form.submit()
        self.assertEqual(response.url, self.url)
        response_message = response._headers['Set-Cookie']
        event_name_empty_msg = "Event Name cannot be empty"
        event_desc_empty_msg = "Event Description cannot be empty"
        event_date_empty_msg = "Event Dates cannot be empty"
        self.assertTrue(event_name_empty_msg in response_message)
        self.assertTrue(event_desc_empty_msg in response_message)
        self.assertTrue(event_date_empty_msg in response_message)

    def test_success_PTO_submit(self):
        self.form.set('event_name', 'China')
        self.form.set('event_description', 'Travel to China')
        self.form.set('date_begin', '07/01/2017')
        self.form.set('date_end', '07/15/2017')
        response = self.form.submit()
        response_message = response._headers['Set-Cookie']
        schedule = Schedule.objects.filter(event_name='China').first()
        self.assertEqual(response.url, self.url)
        self.assertTrue(schedule)
        self.assertEqual(schedule.event_desc, 'Travel to China')
        self.assertTrue("Information successfully updated" in response_message)
        schedule.delete()
