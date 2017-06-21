from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client

from app.tests.mixins import AuthRouteTestingWithKwargs

from app.views import user_retirement_views


class PassingWrongArgumentRegressionTests(TestCase, AuthRouteTestingWithKwargs):
    def setUp(self):
        """ Class for testing api index view"""
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:user_retirement_index'
        self.route = '/users/55/retirement'
        self.view = user_retirement_views.user_retirement_index
        self.responses = {
            'exists': 200,
            'GET': 200,
            'POST': 200,
            'PUT': 405,
            'PATCH': 405,
            'DELETE': 405,
            'HEAD': 405,
            'OPTIONS': 405,
            'TRACE': 405
        }
        self.kwargs = {'user_id': 55}
        self.expected_response_content = 'User 55 retirement index'
        AuthRouteTestingWithKwargs.__init__(self)

    def dummy_function_that_represents_a_view(self, user_id):
        return type(user_id) is int

    def test_kwarg_type_is_correct(self):
        self.assertTrue(self.dummy_function_that_represents_a_view(**self.kwargs))
