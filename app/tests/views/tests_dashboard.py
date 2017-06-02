# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

import app.views as v


class DashboardTests(TestCase):

    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_get(self):
        request = self.factory.get('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_post(self):
        request = self.factory.post('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_put(self):
        request = self.factory.put('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_delete(self):
        request = self.factory.delete('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_head(self):
        request = self.factory.head('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_options(self):
        request = self.factory.options('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_trace(self):
        request = self.factory.trace('/dashboard')
        response = v.dashboard_home(request)
        self.assertEqual(response.status_code, 405)
