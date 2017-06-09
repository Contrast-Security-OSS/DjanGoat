# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import pytz
import datetime
from app.tests.mixins import Pep8ModelTests, ModelCrudTests
from app.models import Benefits


class AnalyticsModelTests(TestCase, Pep8ModelTests, ModelCrudTests):
    def setUp(self):
        # Path to file of model
        self.path = "app/models/Benefits/benefits.py"
        self.created_at = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.updated_at = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = Benefits.objects.create(created_at=self.created_at, updated_at=self.updated_at)
        self.model.save()
        self.attributes = ["created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = pytz.utc.localize(datetime.datetime(2017, 7, 4, 0, 0))
        self.parent = None
