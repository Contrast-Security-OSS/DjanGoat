# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.urls import reverse

# Create your tests here.
class BasicAppTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
