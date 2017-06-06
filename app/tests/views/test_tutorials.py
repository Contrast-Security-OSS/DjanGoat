# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse
from app.tests.mixins import RouteTestingMixin
from app.tests.mixins import RouteTestingWithKwargs


import app.views as views

tutorials = views.tutorials_views


class TutorialTestsIndex(TestCase, RouteTestingMixin):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_index'
        self.route = '/tutorial'
        self.view = tutorials.index
        self.responses = [200, 200, 405, 405, 405, 405, 405, 405]


class TutorialsCredentialsTests(TestCase, RouteTestingMixin):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_credentials'
        self.route = '/tutorials/credentials'
        self.view = tutorials.credentials
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


class TutorialsIdTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_id'
        self.route = '/tutorials/100'
        self.view = tutorials.id
        self.responses = [200, 405, 200, 200, 200, 405, 405, 405]
        self.kwargs = {'id_number': 22}
        self.parameter = "100"


class TutorialsIdEditsTests(TestCase, RouteTestingWithKwargs):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_id_edit'
        self.route = '/tutorials/100/edit'
        self.view = tutorials.id_edit
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]
        self.kwargs = {'id_number': 22}
        self.parameter = "100"


class TutorialsNewTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:tutorials_new'
        self.route = '/tutorials/new'
        self.view = tutorials.new
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]
