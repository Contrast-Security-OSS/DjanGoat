# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

import app.views as views

dashboard = views.dashboard_views


# Tests checking that that '/dashboard' properly handles HttpRequests
# Accepts Both GET and POST requests and refuses all others with an error code 405 (Method not allowed)
class DashboardIndexHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard index
    # and ensuring the response code is 200 (OK)
    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:dashboard_index'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_get(self):
        request = self.factory.get('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_post(self):
        request = self.factory.post('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_index_put(self):
        request = self.factory.put('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_delete(self):
        request = self.factory.delete('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_head(self):
        request = self.factory.head('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_options(self):
        request = self.factory.options('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_trace(self):
        request = self.factory.trace('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_index_patch(self):
        request = self.factory.patch('/dashboard')
        response = dashboard.index(request)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/dashboard/home' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardHomeHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/home
    # and ensuring the response code is 200 (OK)
    def test_dashboard_home_route_exists(self):
        response = self.client.get(reverse('app:dashboard_home'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_home_get(self):
        request = self.factory.get('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_home_post(self):
        request = self.factory.post('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_put(self):
        request = self.factory.put('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_delete(self):
        request = self.factory.delete('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_head(self):
        request = self.factory.head('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_options(self):
        request = self.factory.options('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_trace(self):
        request = self.factory.trace('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_home_patch(self):
        request = self.factory.patch('/dashboard/home')
        response = dashboard.home(request)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/dashboard/change_graph' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardChangeGraphHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/change_graph
    # and ensuring the response code is 200 (OK)
    def test_dashboard_change_graph_route_exists(self):
        response = self.client.get(reverse('app:dashboard_change_graph'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_change_graph_get(self):
        request = self.factory.get('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_change_graph_post(self):
        request = self.factory.post('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_put(self):
        request = self.factory.put('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_delete(self):
        request = self.factory.delete('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_head(self):
        request = self.factory.head('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_options(self):
        request = self.factory.options('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_trace(self):
        request = self.factory.trace('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_change_graph_patch(self):
        request = self.factory.patch('/dashboard/change_graph')
        response = dashboard.change_graph(request)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/dashboard/doc' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardDocHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/doc
    # and ensuring the response code is 200 (OK)
    def test_dashboard_doc_route_exists(self):
        response = self.client.get(reverse('app:dashboard_doc'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_doc_get(self):
        request = self.factory.get('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_doc_post(self):
        request = self.factory.post('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_put(self):
        request = self.factory.put('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_delete(self):
        request = self.factory.delete('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_head(self):
        request = self.factory.head('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_options(self):
        request = self.factory.options('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_trace(self):
        request = self.factory.trace('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_doc_patch(self):
        request = self.factory.patch('/dashboard/doc')
        response = dashboard.doc(request)
        self.assertEqual(response.status_code, 405)


# Tests checking that that '/dashboard/new' properly handles HttpRequests
# Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
class DashboardNewHttpRequestMethodTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard/new
    # and ensuring the response code is 200 (OK)
    def test_dashboard_new_route_exists(self):
        response = self.client.get(reverse('app:dashboard_new'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_new_get(self):
        request = self.factory.get('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_new_post(self):
        request = self.factory.post('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_put(self):
        request = self.factory.put('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_delete(self):
        request = self.factory.delete('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_head(self):
        request = self.factory.head('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_options(self):
        request = self.factory.options('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_trace(self):
        request = self.factory.trace('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_new_patch(self):
        request = self.factory.patch('/dashboard/new')
        response = dashboard.new_dashboard(request)
        self.assertEqual(response.status_code, 405)


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
