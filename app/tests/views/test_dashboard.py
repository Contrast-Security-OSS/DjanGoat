# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from app.tests.Mixins import RouteTestingMixin

import app.views as views

dashboard = views.dashboard_views


# Tests checking that that '/dashboard' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class DashboardIndexHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_index'
        self.route = '/dashboard'
        self.view = dashboard.index
        self.responses = [200, 200, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/home' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardHomeHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_home'
        self.route = '/dashboard/home'
        self.view = dashboard.home
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/change_graph' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardChangeGraphHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_change_graph'
        self.route = '/dashboard/change_graph'
        self.view = dashboard.change_graph
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/doc' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardDocHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_doc'
        self.route = '/dashboard/doc'
        self.view = dashboard.doc
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardNewHttpRequestMethodTests(TestCase, RouteTestingMixin):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:dashboard_new'
        self.route = '/dashboard/new'
        self.view = dashboard.new_dashboard
        self.responses = [200, 405, 405, 405, 405, 405, 405, 405]


# Tests checking that that '/dashboard/:id/edit' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DashboardEditHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/55/edit
    # and ensuring the response code is 200 (OK)
    def test_dashboard_edit_route_exists(self):
        response = self.client.get(reverse('app:dashboard_edit', kwargs={'dashboard_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_edit_get(self):
        request = self.factory.get('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_edit_post(self):
        request = self.factory.post('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_put(self):
        request = self.factory.put('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_delete(self):
        request = self.factory.delete('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_head(self):
        request = self.factory.head('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_options(self):
        request = self.factory.options('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_trace(self):
        request = self.factory.trace('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_edit_patch(self):
        request = self.factory.patch('/dashboard/55/edit')
        response = dashboard.edit_dashboard(request, 55)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/dashboard/:id' properly handles HttpRequests
# Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class DashboardViewHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/55/
    # and ensuring the response code is 200 (OK)
    def test_dashboard_view_route_exists(self):
        response = self.client.get(reverse('app:dashboard_view', kwargs={'dashboard_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_get(self):
        request = self.factory.get('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_post(self):
        request = self.factory.post('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_view_put(self):
        request = self.factory.put('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_delete(self):
        request = self.factory.delete('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_head(self):
        request = self.factory.head('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_view_options(self):
        request = self.factory.options('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_view_trace(self):
        request = self.factory.trace('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_view_patch(self):
        request = self.factory.patch('/dashboard/55')
        response = dashboard.dashboard_view(request, 55)
        self.assertEqual(response.status_code, 200)
