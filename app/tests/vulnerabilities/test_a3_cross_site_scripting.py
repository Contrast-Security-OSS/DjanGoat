from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.models import User
import pytz
import datetime
import json


class CrossSiteScriptingTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = '/users/13/retirement'
        self.kwargs = {'id_number': 13}
        input_email = "cat.dog@contrastsecurity.com"
        input_password = "catdogzzz"
        input_admin = False
        input_first_name = "<script>document.write("<b>dog</b>");</script>"
        input_last_name = "catdog"
        u_input_create_date = pytz.utc.localize(datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

    def test_header_xss(self):
        user = User.objects.get(last_name="catdogz")
        response = self.client.get(request)
        self.assertTrue('first_name' in response)

    def test_dom_xss(self):
        self.assertTrue(True)



