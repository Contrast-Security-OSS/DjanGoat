from django.test import TestCase, RequestFactory, Client
from app.models import User
from app.views import sessions_views as sessions
import pytz
import datetime


class TestMissingFunctionLevelAccessControl(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    # Simulate logging in as a normal user and switching to a different user
    def test_route_post(self):
        # Create user in database
        input_email = "ryan.dens@contrastsecurity.com"
        input_password = "12345"
        input_admin = False
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        factory_request = self.factory.post('/sessions/')
        factory_response = sessions.sessions_index(factory_request, email="ryan.dens@contrastsecurity.com",
                                                   password="12345", path="/dashboard/home")
        self.assertEqual(factory_response.status_code, 302)

        client_request = self.client.post('/sessions/',
                                          {'email': 'ryan.dens@contrastsecurity.com', 'password': '12345',
                                           'path': '/admin/1/dashboard/'},
                                          follow=True)
        self.assertEqual(client_request.status_code, 200)
