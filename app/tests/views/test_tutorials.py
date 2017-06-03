# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from django.urls import reverse

import app.views as v


class TutorialTestsIndex(TestCase):

    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_tutorials_get(self):
        request = self.factory.get('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_post(self):
        request = self.factory.post('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_put(self):
        request = self.factory.put('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_delete(self):
        request = self.factory.delete('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_head(self):
        request = self.factory.head('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_options(self):
        request = self.factory.options('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 405)

    def test_dashboard_trace(self):
        request = self.factory.trace('/tutorials')
        response = v.tutorials_index(request)
        self.assertEqual(response.status_code, 405)


class TutorialsCredentialsTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_tutorials_credentials_get(self):
        request = self.factory.get('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 200)

    def test_tutorials_credentials_post(self):
        request = self.factory.post('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_credentials_put(self):
        request = self.factory.put('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_credentials_delete(self):
        request = self.factory.delete('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_credentials_head(self):
        request = self.factory.head('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_credentials_options(self):
        request = self.factory.options('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_credentials_trace(self):
        request = self.factory.trace('/tutorials/credentials')
        response = v.tutorials_credentials(request)
        self.assertEqual(response.status_code, 405)


class TutorialsIdTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_tutorials_id_get(self):
        request = self.factory.get('/tutorials/100')
        response = v.tutorials_id(request, "100")
        self.assertEqual(response.status_code, 200)

    def test_tutorials_id_post(self):
        request = self.factory.post('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_id_put(self):
        request = self.factory.put('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 200)

    def test_tutorials_id_delete(self):
        request = self.factory.delete('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 200)

    def test_tutorials_id_head(self):
        request = self.factory.head('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_id_options(self):
        request = self.factory.options('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_id_trace(self):
        request = self.factory.trace('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_id_patch(self):
        request = self.factory.patch('/tutorials/20')
        response = v.tutorials_id(request, "20")
        self.assertEqual(response.status_code, 200)


class TutorialsIdEditsTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_tutorials_edit_id_get(self):
        request = self.factory.get('/tutorials/100/edit')
        response = v.tutorials_id_edit(request, "100")
        self.assertEqual(response.status_code, 200)

    def test_tutorials_edit_id_post(self):
        request = self.factory.post('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_put(self):
        request = self.factory.put('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_delete(self):
        request = self.factory.delete('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_head(self):
        request = self.factory.head('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_options(self):
        request = self.factory.options('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_trace(self):
        request = self.factory.trace('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edits_id_patch(self):
        request = self.factory.patch('/tutorials/20/edit')
        response = v.tutorials_id_edit(request, "20")
        self.assertEqual(response.status_code, 405)


class TutorialsNewTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_tutorials_edit_id_get(self):
        request = self.factory.get('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 200)

    def test_tutorials_edit_id_post(self):
        request = self.factory.post('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_put(self):
        request = self.factory.put('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_delete(self):
        request = self.factory.delete('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_head(self):
        request = self.factory.head('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_options(self):
        request = self.factory.options('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edit_id_trace(self):
        request = self.factory.trace('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)

    def test_tutorials_edits_id_patch(self):
        request = self.factory.patch('/tutorials/new')
        response = v.tutorials_new(request)
        self.assertEqual(response.status_code, 405)


