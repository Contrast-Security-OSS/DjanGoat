# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

import app.views as views

# print(views.users_views)
retirement = views.user_retirement_views

# Tests checking that that '/users/:user_id/retirement' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserRetirementIndexRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/retirement/
    # and ensuring the response code is 200 (OK)
    def test_user_retirement_index_route_exists(self):
        response = self.client.get(reverse('app:user_retirement_index', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_user_retirement_index_get(self):
        request = self.factory.get('/users/55/retirement')
        response = retirement.user_retirement_index(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_retirement_index_post(self):
        request = self.factory.post('/users/55/retirement')
        response = retirement.user_retirement_index(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_retirement_index_put(self):
        request = self.factory.put('/users/55/retirement')
        response = retirement.user_retirement_index(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_retirement_index_delete(self):
        request = self.factory.delete('/users/55/retirement')
        response = retirement.user_retirement_index(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_retirement_index_patch(self):
        request = self.factory.patch('/users/55/retirement')
        response = retirement.user_retirement_index(request, 55)
        self.assertEqual(response.status_code, 405)


# # Tests checking that that '/users/:id/retirement/new' properly handles HttpRequests and routing
# # Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on id #55
# class UserNewMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/retirement/new
#     # and ensuring the response code is 200 (OK)
#     def test_user_new_message_route_exists(self):
#         response = self.client.get(reverse('app:new_user_message', kwargs={'user_id': 55}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_new_message_get(self):
#         request = self.factory.get('/users/55/retirement/new')
#         response = retirement.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_new_message_post(self):
#         request = self.factory.post('/users/55/retirement/new')
#         response = retirement.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_put(self):
#         request = self.factory.put('/users/55/retirement/new')
#         response = retirement.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_delete(self):
#         request = self.factory.delete('/users/55/retirement/new')
#         response = retirement.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_patch(self):
#         request = self.factory.patch('/users/55/retirement/new')
#         response = retirement.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
# # Tests checking that that '/users/:user_id/retirement/message_id/edit' properly handles HttpRequests and routing
# # Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on user_id 55 and message_id 22
# class UserEditMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/retirement/22/edit
#     # and ensuring the response code is 200 (OK)
#     def test_user_edit_message_route_exists(self):
#         response = self.client.get(reverse('app:edit_user_message', kwargs={'user_id': 55, 'message_id': 22}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_edit_message_get(self):
#         request = self.factory.get('/users/55/retirement/22/edit')
#         response = retirement.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_edit_message_post(self):
#         request = self.factory.post('/users/55/retirement/22/edit')
#         response = retirement.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_put(self):
#         request = self.factory.put('/users/55/retirement/22/edit')
#         response = retirement.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_delete(self):
#         request = self.factory.delete('/users/55/retirement/22/edit')
#         response = retirement.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_patch(self):
#         request = self.factory.patch('/users/55/retirement/22/edit')
#         response = retirement.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
# # Tests checking that that '/users/:user_id/retirement/message_id' properly handles HttpRequests and routing
# # Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on user_id 55 and message_id 22
# class UserShowMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/retirement/22
#     # and ensuring the response code is 200 (OK)
#     def test_user_message_route_exists(self):
#         response = self.client.get(reverse('app:user_message', kwargs={'user_id': 55, 'message_id': 22}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_get(self):
#         request = self.factory.get('/users/55/retirement/22')
#         response = retirement.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_post(self):
#         request = self.factory.post('/users/55/retirement/22')
#         response = retirement.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_message_put(self):
#         request = self.factory.put('/users/55/retirement/22')
#         response = retirement.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_delete(self):
#         request = self.factory.delete('/users/55/retirement/22')
#         response = retirement.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_patch(self):
#         request = self.factory.patch('/users/55/retirement/22')
#         response = retirement.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
