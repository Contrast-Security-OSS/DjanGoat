from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, RequestFactory
from app.views import sessions_views as sessions
from app.models.User.user import User
import datetime
import pytz


class TestCredentialEnumeration(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        input_email = "ziyang.wang@example.com"
        input_password = "123456"
        input_admin = True
        input_first_name = "Ziyang"
        input_last_name = "Wang"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
            )

    def test_bad_password(self):
        request = self.factory.post('/sessions/')
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = sessions.sessions_index(request, email="ziyang.wang@example.com",
                                           password="1234", path="/dashboard")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['message'], "Password incorrect!")

    def test_bad_email(self):
        request = self.factory.post('/sessions/')
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = sessions.sessions_index(request, email="ziyang.w@example.com",
                                           password="123456", path="/dashboard")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['message'], "Email incorrect!")
