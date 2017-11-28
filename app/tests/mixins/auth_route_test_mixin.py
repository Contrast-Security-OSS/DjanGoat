from app.tests.mixins.route_test_mixin import RouteTestingWithKwargs
from app.views import sessions_views as sessions
from app.models.User.user import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import reverse
import datetime
import pytz


# Mixin for testing the creation of routes
# Make sure your kwargs match your variable argument
class AuthRouteTestingWithKwargs(RouteTestingWithKwargs):
    mixin_model = None
    not_logged_in_message = "Fill out the form below to login to your control panel"
    no_longer_logged_in_message = "Fill out the form below to login to your control panel"
    bad_auth_message = "Email or password incorrect!"

    def __init__(self):
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.mixin_model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    @staticmethod
    def add_messages_middleware(request):
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

    def test_route_exists(self):
        response = self.client.get(reverse(self.route_name, kwargs=self.kwargs), follow=True)
        self.assertEqual(response.status_code, self.responses['exists'])

    def test_route_get(self):
        if(self.responses['GET'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_get()
        else:
            request = self.factory.get(self.route, follow=True)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_post(self):
        if(self.responses['POST'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_post()
        else:
            request = self.factory.post(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_put(self):
        if(self.responses['PUT'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_put()
        else:
            request = self.factory.put(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_patch(self):
        if(self.responses['PATCH'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_patch()
        else:
            request = self.factory.patch(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_delete(self):
        if(self.responses['DELETE'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_delete()
        else:
            request = self.factory.delete(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_head(self):
        if(self.responses['HEAD'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_head()
        else:
            request = self.factory.head(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_options(self):
        if(self.responses['OPTIONS'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_options()
        else:
            request = self.factory.options(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def test_route_trace(self):
        if(self.responses['TRACE'] != 200):
            super(AuthRouteTestingWithKwargs, self).test_route_trace()
        else:
            request = self.factory.trace(self.route)
            AuthRouteTestingWithKwargs.add_messages_middleware(request)
            self.no_auth_test(request)
            self.good_auth_test(request)
            self.old_auth_test(request)
            self.bad_password_test(request)
            self.bad_email_test(request)

    def no_auth_test(self, request):
        response = self.view(request, **self.kwargs)
        # We should be redirected
        self.assertEqual(response.status_code, 302)
        # Make a new request to the location of the redirect
        redirect_response = self.client.get(response['LOCATION'], follow=True)
        # Check to make sure the response is correct
        self.assertContains(redirect_response, self.not_logged_in_message)

    def bad_password_test(self, request):
        """
        Test to make sure a bad password does not create a new session
        :param request: is the request to be completed
        :return: None
        """
        # Create new session
        auth_request = self.factory.post('/sessions/')
        AuthRouteTestingWithKwargs.add_messages_middleware(auth_request)
        auth_response = sessions.sessions_index(auth_request, email="ryan.dens@example.com",
                                                password="1234", path="/dashboard")

        # Make sure new session not created
        self.assertEqual(auth_response.status_code, 302)
        self.assertEqual(auth_response['message'], "Password incorrect!")

        # Error should be raised as no cookie should be set (post to create session failed)
        with self.assertRaises(KeyError) as error:
            request.COOKIES['auth_token'] = auth_response.cookies['auth_token'].value

        self.assertTrue('auth_token' in error.exception)

    def bad_email_test(self, request):
        # Create new session
        auth_request = self.factory.post('/sessions/')
        AuthRouteTestingWithKwargs.add_messages_middleware(auth_request)
        auth_response = sessions.sessions_index(auth_request, email="ryan.den@example.com",
                                                       password="12345", path=self.route)

        # Make sure new session not created
        self.assertEqual(auth_response.status_code, 302)
        self.assertEqual(auth_response["message"], "Email incorrect!")

        # Error should be raised as no cookie should be set (post to create session failed)
        with self.assertRaises(KeyError) as error:
            request.COOKIES['auth_token'] = auth_response.cookies['auth_token'].value

        self.assertTrue('auth_token' in error.exception)

    # Test authentication decorator with an old token stored in the user's cookies
    def old_auth_test(self, request):
        # Create new session
        auth_request = self.factory.post('/sessions/')
        AuthRouteTestingWithKwargs.add_messages_middleware(auth_request)
        auth_response = sessions.sessions_index(auth_request, email="ryan.dens@example.com",
                                                   password="12345", path=self.route)
        # Make sure initial redirect was called (but not followed)
        self.assertEqual(auth_response.status_code, 302)

        # Generate a new token for the user, the old token has expired and is not valid
        self.mixin_model.generate_token()
        self.mixin_model.save()

        # Add the old auth token cookie to the request
        request.COOKIES['auth_token'] = auth_response.cookies['auth_token'].value
        response = self.view(request, **self.kwargs)

        # We should be redirected
        self.assertEqual(response.status_code, 302)

        # Make a new request to the location of the redirect
        redirect_response = self.client.get(response['LOCATION'], follow=True)
        # Check to make sure the response is correct
        self.assertContains(redirect_response, self.not_logged_in_message)

    def good_auth_test(self, request):
        # Create new session
        auth_request = self.factory.post('/sessions/')
        AuthRouteTestingWithKwargs.add_messages_middleware(auth_request)

        auth_response = sessions.sessions_index(
            auth_request, email="ryan.dens@example.com",
            password="12345", path=self.route
        )

        # Make sure redirect was called (but not followed)
        self.assertEqual(auth_response.status_code, 302)
        # Add auth token cookie to request
        request.COOKIES['auth_token'] = auth_response.cookies['auth_token'].value
        response = self.view(request, **self.kwargs)
        # Make sure request contains expected content
        self.assertContains(response, self.expected_response_content, status_code=200)
