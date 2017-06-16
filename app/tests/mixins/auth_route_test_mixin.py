from django.urls import reverse
import pytz
import datetime
from app.models.User.user import User
from app.views import sessions_views as sessions

# Mixin for testing the creation of routes
# Make sure your kwargs match your variable argument
class AuthRouteTestingWithKwargs(object):
    mixin_model = None

    def __init__(self):
        input_email = "ryan.dens@contrastsecurity.com"
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

    # Tries to verify a route exists to a place without an auth_token
    def test_route_exists_no_auth(self):
        response = self.client.get(reverse(self.route_name, kwargs=self.kwargs))
        self.assertContains(response, "Sorry, but you are not logged in. Please log in again", status_code=self.responses['exists'])

    def test_route_exists_bad_password(self):
        factory_request = self.factory.post('/sessions/')
        factory_response = sessions.sessions_index(factory_request, email="ryan.dens@contrastsecurity.com",
                                                   password="1234", path="/dashboard")
        self.assertEqual(factory_response.status_code, 200)
        self.assertEqual(factory_response.content, "Email or password incorrect!")

    def test_route_exists_bad_email(self):
        factory_request = self.factory.post('/sessions/')
        factory_response = sessions.sessions_index(factory_request, email="ryan.den@contrastsecurity.com",
                                                   password="12345", path="/dashboard")
        self.assertEqual(factory_response.status_code, 200)
        self.assertEqual(factory_response.content, "Email or password incorrect!")

    # Manually changes the user's auth token to be different than what the stored cookie is
    def test_route_exists_old_auth(self):
        # Create new session
        factory_request = self.factory.post('/sessions/')
        factory_response = sessions.sessions_index(factory_request, email="ryan.dens@contrastsecurity.com",
                                                   password="12345", path="/dashboard")
        # Make sure redirect was called (but not followed_
        self.assertEqual(factory_response.status_code, 302)

        # Create new request to self.route, changing the token stored in the user's cookies
        # to simulate the auth_token expiring in the database
        new_factory_request = self.factory.get(self.route)
        new_factory_request.COOKIES['auth_token'] = 'old_token'
        new_factory_response = self.view(new_factory_request, *self.kwargs)
        self.assertEqual(new_factory_response.content,
                         "Sorry, but you are no longer logged in to your session. Please log in again")

    def test_route_get(self):
        request = self.factory.get(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['GET'],
                         "your get method for route: " + self.route + " returned: " + str(response.status_code))

    def test_route_post(self):
        request = self.factory.post(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['POST'],
                         "your post method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_put(self):
        request = self.factory.put(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['PUT'],
                         "your put method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_patch(self):
        request = self.factory.patch(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['PATCH'],
                         "your patch method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_delete(self):
        request = self.factory.delete(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['DELETE'],
                         "your delete method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_head(self):
        request = self.factory.head(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['HEAD'],
                         "your head method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_options(self):
        request = self.factory.options(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['OPTIONS'],
                         "your options method for route: " + self.route + "returned: " + str(response.status_code))

    def test_route_trace(self):
        request = self.factory.trace(self.route)
        response = self.view(request, *self.kwargs)
        self.assertEqual(response.status_code, self.responses['TRACE'],
                         "your options method for route: " + self.route + "returned: " + str(response.status_code))
