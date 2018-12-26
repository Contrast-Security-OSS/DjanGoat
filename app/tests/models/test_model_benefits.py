# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
import pytz
import datetime
from app.tests.mixins import Pep8ModelTests, ModelCrudTests
from app.models import Benefits
from django.conf import settings
import filecmp
import os


class BenefitsModelTests(TestCase, Pep8ModelTests, ModelCrudTests):

    def setUp(self):
        # Path to file of model
        self.path = "app/models/Benefits/benefits.py"
        self.created_at = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))
        self.updated_at = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))
        self.model = Benefits.objects.create(
            created_at=self.created_at, updated_at=self.updated_at)
        self.attributes = ["created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = pytz.utc.localize(
            datetime.datetime(2017, 7, 4, 0, 0))
        self.parent = None
        self.factory = RequestFactory()

    # silence_streams is not tested here
    # it works as a decorator that redirects STDERR
    def test_benefits_methods(self):
        # Upload file
        route = "/upload"
        enctype = "multipart/form-data"
        origin_file_name = "app/__init__.py"
        origin_file = open(origin_file_name, "rb")
        request = self.factory.post(
            route, {'enctype': enctype, 'file': origin_file})
        origin_file.close()
        uploaded_file = request.FILES['file']

        data_path = os.path.join(settings.MEDIA_ROOT, "data")
        full_file_name = os.path.join(data_path, uploaded_file.name)
        # expects no __init.py__ in MEDIA_ROOT/data
        if os.path.isfile(full_file_name):
            os.remove(full_file_name)
        # Testing save_data
        Benefits.save_data(uploaded_file)
        self.assertEqual(os.path.isfile(full_file_name), True)
        self.assertEqual(filecmp.cmp(origin_file_name, full_file_name), True)
        os.remove(full_file_name)
        # Testing make_backup
        bak_file_path = Benefits.save_data(uploaded_file, backup="true")
        self.assertNotEqual(bak_file_path, None)
        self.assertEqual(os.path.isfile(bak_file_path), True)
        os.remove(full_file_name)
        os.remove(bak_file_path)
