# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory
import pytz
import datetime
from app.tests.mixins import Pep8ModelTests, ModelCrudTests
from app.models import Benefits, User
from django.conf import settings
import filecmp
import os
import time


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
        self.model.save()
        self.attributes = ["created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = pytz.utc.localize(
            datetime.datetime(2017, 7, 4, 0, 0))
        self.parent = None
        self.factory = RequestFactory()

    def test_save_data(self):
        # Upload file
        route = "/upload"
        enctype = "multipart/form-data"
        origin_file = "app/__init__.py"
        file = open(origin_file, "rb")
        request = self.factory.post(
            route, {'enctype': enctype, 'file': file})
        file.close()
        uploaded_file = request.FILES['file']

        # Remove file if already existed, for testing purpose
        data_path = os.path.join(settings.MEDIA_ROOT, "data")
        full_file_name = os.path.join(data_path, uploaded_file.name)
        if os.path.isfile(full_file_name):
            os.remove(full_file_name)

        # Testing save_data
        Benefits.save_data(uploaded_file)
        self.assertEqual(os.path.isfile(full_file_name), True)
        self.assertEqual(filecmp.cmp(origin_file, full_file_name), True)

        # Testing make_backup
        os.remove(full_file_name)
        epoch_time = int(time.time())
        Benefits.save_data(uploaded_file, backup="true")
        # expects the backup file created within a second
        # need a better way testing
        bak_file_name1 = "%s/bak%d_%s" % (data_path,
                                          epoch_time, uploaded_file.name)
        bak_file_name2 = "%s/bak%d_%s" % (data_path,
                                          epoch_time+1, uploaded_file.name)
        test_result = os.path.isfile(
            bak_file_name1) or os.path.isfile(bak_file_name2)
        self.assertEqual(test_result, True)
        os.remove(full_file_name)
        try:
            os.remove(bak_file_name1)
        except:
            os.remove(bak_file_name2)
