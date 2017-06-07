from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from app.tests.mixins import RouteTestingWithKwargs

import app.views as views

sessions = views.sessions_views


class TestLogin(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:login'
        self.route = '/login'
        self.view = sessions.login
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


class TestLogout(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:logout'
        self.route = '/logout'
        self.view = sessions.login
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


class SessionsIndexTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:sessions_index'
        self.route = '/sessions'
        self.view = sessions.sessions_index
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


class SessionsNewTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:sessions_new'
        self.route = '/sessions/new'
        self.view = sessions.new_sessions
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


class SessionsIdEditTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:sessions_edit'
        self.route = '/sessions/5/edit'
        self.view = sessions.edit_session
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
        self.kwargs = {'id_number': 5}


class SessionsIdTest(TestCase, RouteTestingWithKwargs):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:session_id'
        self.route = '/sessions/5'
        self.view = sessions.session_id
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
        self.kwargs = {'id_number': 5}
