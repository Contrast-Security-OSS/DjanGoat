# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
from app.models import Benefits
from django.conf import settings
import os


class CommandInjectionTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_benefits_methods(self):
        # Setting up
        route = "/upload"
        enctype = "multipart/form-data"
        origin_file = "app/__init__.py; mkdir hacked; cp"
        new_file_path = os.path.join(settings.BASE_DIR, origin_file)
        create_new_file = open(new_file_path, "w+")
        create_new_file.close()
        # Send POST request
        new_file = open(new_file_path, "rb")
        request = self.factory.post(
            route, {'enctype': enctype, 'file': new_file})
        new_file.close()
        # Testing saved file exists and hacked file exists
        uploaded_file = request.FILES['file']
        data_path = os.path.join(settings.MEDIA_ROOT, "data")
        full_file_name = os.path.join(data_path, uploaded_file.name)
        # Where command line executed
        Benefits.save_data(uploaded_file, backup="true")
        self.assertTrue(os.path.isfile(full_file_name))
        hacked_dir = os.path.join(settings.BASE_DIR, 'hacked')
        self.assertTrue(os.path.isdir(hacked_dir))
        # Cleanup
        os.remove(new_file_path)
        os.remove(full_file_name)
        os.rmdir(hacked_dir)
