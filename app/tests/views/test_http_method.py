from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
import app.views as v


class HttpMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:index'
        self.route = '/'
        self.view = v.app_index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 200,
            'PATCH': 200,
            'DELETE': 200,
            'HEAD': 200,
            'OPTIONS': 200,
            'TRACE': 200
        }
        self.kwargs = {}
