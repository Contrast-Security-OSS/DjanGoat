from __future__ import unicode_literals
from django.test import TestCase, RequestFactory, Client
from app.models import User
import pytz
import datetime
import json


class CrossSiteScriptingTest(TestCase):
    def setUp(self):
        self.param = {'email': 'catdog@gmail.com', 'first_name': '<script>alert(1)</script>',
                      'last_name': 'dog', 'password': '123456',
                      'confirm': '123456'}
        page = self.app.get('/signup/')
        self.assertEqual(len(page.forms), 1)
        form = page.forms[0]
        form.set('email', self.param['email'])
        form.set('first_name', self.param['first_name'])
        form.set('last_name', self.param['last_name'])
        form.set('password', self.param['password'])
        form.set('confirm', self.param['confirm'])
        self.form = form

    def test_header_xss(self):
        response = self.form.submit()
        user = User.objects.filter(email=self.param['first_name'])
        self.assertTrue(user)
        self.assertContains(self, response, '<script>alert(1)</script>')
        self.assertNotContains(self, response,
                               '&lt;script&gt;alert(1)&lt;/script&gt;')
        user.first().delete()

