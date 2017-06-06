# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

import app.views as views

# print(views.users_views)
benefit_forms = views.user_benefit_forms_views

# Tests checking that that '/users/:id/benefit_forms' properly handles HttpRequests and routing
# Accepts GET and POST requests and refuses all others with an error code 405 (Method not allowed)
# Tested on id #55
class UserMessagesRoutingAndHttpTests(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Verifies the route exists by getting the users/55/messages/
    # and ensuring the response code is 200 (OK)
    def test_user_messages_route_exists(self):
        response = self.client.get(reverse('app:user_benefit_forms', kwargs={'user_id': 55}))
        self.assertEqual(response.status_code, 200)

    def test_user_messages_get(self):
        request = self.factory.get('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_messages_post(self):
        request = self.factory.post('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 200)

    def test_user_messages_put(self):
        request = self.factory.put('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_messages_delete(self):
        request = self.factory.delete('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)

    def test_user_messages_patch(self):
        request = self.factory.patch('/users/55/benefit_forms')
        response = benefit_forms.user_benefit_forms(request, 55)
        self.assertEqual(response.status_code, 405)


# # Tests checking that that '/users/:id/messages/new' properly handles HttpRequests and routing
# # Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on id #55
# class UserNewMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/messages/new
#     # and ensuring the response code is 200 (OK)
#     def test_user_new_message_route_exists(self):
#         response = self.client.get(reverse('app:new_user_message', kwargs={'user_id': 55}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_new_message_get(self):
#         request = self.factory.get('/users/55/messages/new')
#         response = benefit_forms.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_new_message_post(self):
#         request = self.factory.post('/users/55/messages/new')
#         response = benefit_forms.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_put(self):
#         request = self.factory.put('/users/55/messages/new')
#         response = benefit_forms.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_delete(self):
#         request = self.factory.delete('/users/55/messages/new')
#         response = benefit_forms.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_new_message_patch(self):
#         request = self.factory.patch('/users/55/messages/new')
#         response = benefit_forms.new_user_message(request, 55)
#         self.assertEqual(response.status_code, 405)

# # Tests checking that that '/users/:user_id/messages/message_id/edit' properly handles HttpRequests and routing
# # Accepts GET requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on user_id 55 and message_id 22
# class UserEditMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/messages/22/edit
#     # and ensuring the response code is 200 (OK)
#     def test_user_edit_message_route_exists(self):
#         response = self.client.get(reverse('app:edit_user_message', kwargs={'user_id': 55, 'message_id': 22}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_edit_message_get(self):
#         request = self.factory.get('/users/55/messages/22/edit')
#         response = benefit_forms.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_edit_message_post(self):
#         request = self.factory.post('/users/55/messages/22/edit')
#         response = benefit_forms.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_put(self):
#         request = self.factory.put('/users/55/messages/22/edit')
#         response = benefit_forms.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_delete(self):
#         request = self.factory.delete('/users/55/messages/22/edit')
#         response = benefit_forms.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_edit_message_patch(self):
#         request = self.factory.patch('/users/55/messages/22/edit')
#         response = benefit_forms.edit_user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
# # Tests checking that that '/users/:user_id/messages/message_id' properly handles HttpRequests and routing
# # Accepts GET, PATCH, PUT, and DELETE requests and refuses all others with an error code 405 (Method not allowed)
# # Tested on user_id 55 and message_id 22
# class UserShowMessageRoutingAndHttpTests(TestCase):
#     # setup for all test cases
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.client = Client()
#
#     # Verifies the route exists by getting the users/55/messages/22
#     # and ensuring the response code is 200 (OK)
#     def test_user_message_route_exists(self):
#         response = self.client.get(reverse('app:user_message', kwargs={'user_id': 55, 'message_id': 22}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_get(self):
#         request = self.factory.get('/users/55/messages/22')
#         response = benefit_forms.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_post(self):
#         request = self.factory.post('/users/55/messages/22')
#         response = benefit_forms.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 405)
#
#     def test_user_message_put(self):
#         request = self.factory.put('/users/55/messages/22')
#         response = benefit_forms.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_delete(self):
#         request = self.factory.delete('/users/55/messages/22')
#         response = benefit_forms.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
#
#     def test_user_message_patch(self):
#         request = self.factory.patch('/users/55/messages/22')
#         response = benefit_forms.user_message(request, 55, 22)
#         self.assertEqual(response.status_code, 200)
