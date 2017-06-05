# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

import app.views as views

tutorials = views.tutorials_views


class TutorialTestsIndex(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the dashboard index
    # and ensuring the response code is 200 (OK)
    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:tutorials_index'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        request = self.factory.get('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_post(self):
        request = self.factory.post('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_put(self):
        request = self.factory.put('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_delete(self):
        request = self.factory.delete('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_head(self):
        request = self.factory.head('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_options(self):
        request = self.factory.options('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_trace(self):
        request = self.factory.trace('/tutorials')
        response = tutorials.index(request)
        self.assertEqual(response.status_code, 405)


class TutorialsCredentialsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:tutorials_credentials'))
        self.assertEqual(response.status_code, 200)

    def test_credentials_get(self):
        request = self.factory.get('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 200)

    def test_credentials_post(self):
        request = self.factory.post('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_credentials_put(self):
        request = self.factory.put('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_credentials_delete(self):
        request = self.factory.delete('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_credentials_head(self):
        request = self.factory.head('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_credentials_options(self):
        request = self.factory.options('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_credentials_trace(self):
        request = self.factory.trace('/tutorials/credentials')
        response = tutorials.credentials(request)
        self.assertEqual(response.status_code, 405)


class TutorialsIdTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:tutorials_id', kwargs={'id_number': 22}))
        self.assertEqual(response.status_code, 200)

    def test_id_get(self):
        request = self.factory.get('/tutorials/100')
        response = tutorials.id(request, "100")
        self.assertEqual(response.status_code, 200)

    def test_id_post(self):
        request = self.factory.post('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_id_put(self):
        request = self.factory.put('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 200)

    def test_id_delete(self):
        request = self.factory.delete('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 200)

    def test_id_head(self):
        request = self.factory.head('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_id_options(self):
        request = self.factory.options('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_id_trace(self):
        request = self.factory.trace('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_id_patch(self):
        request = self.factory.patch('/tutorials/20')
        response = tutorials.id(request, "20")
        self.assertEqual(response.status_code, 200)


class TutorialsIdEditsTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:tutorials_id_edit', kwargs={'id_number': 22}))
        self.assertEqual(response.status_code, 200)

    def test_edit_id_get(self):
        request = self.factory.get('/tutorials/100/edit')
        response = tutorials.id_edit(request, "100")
        self.assertEqual(response.status_code, 200)

    def test_edit_id_post(self):
        request = self.factory.post('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edit_id_put(self):
        request = self.factory.put('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edit_id_delete(self):
        request = self.factory.delete('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edit_id_head(self):
        request = self.factory.head('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edit_id_options(self):
        request = self.factory.options('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edit_id_trace(self):
        request = self.factory.trace('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_edits_id_patch(self):
        request = self.factory.patch('/tutorials/20/edit')
        response = tutorials.id_edit(request, "20")
        self.assertEqual(response.status_code, 405)


class TutorialsNewTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_dashboard_index_route_exists(self):
        response = self.client.get(reverse('app:tutorials_new'))
        self.assertEqual(response.status_code, 200)

    def test_edit_id_get(self):
        request = self.factory.get('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_id_post(self):
        request = self.factory.post('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edit_id_put(self):
        request = self.factory.put('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edit_id_delete(self):
        request = self.factory.delete('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edit_id_head(self):
        request = self.factory.head('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edit_id_options(self):
        request = self.factory.options('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edit_id_trace(self):
        request = self.factory.trace('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)

    def test_edits_id_patch(self):
        request = self.factory.patch('/tutorials/new')
        response = tutorials.new(request)
        self.assertEqual(response.status_code, 405)
