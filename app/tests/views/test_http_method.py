from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse
from app.tests.Mixins import RouteTestingMixin

import app.views as v


class HttpMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:index'
        self.route = '/'
        self.view = v.app_index
        self.responses = [200, 200, 200, 200, 200, 200, 200, 200]
