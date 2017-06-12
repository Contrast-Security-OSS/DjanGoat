# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import pytz
import datetime
from app.tests.mixins import Pep8ModelTests, ModelCrudTests
from app.models import Analytics


class AnalyticsModelTests(TestCase, Pep8ModelTests, ModelCrudTests):
    def setUp(self):
        # Path to file of model
        self.path = "app/models/Analytics/analytics.py"
        self.ip_address = "127.94.0.2"
        self.referrer = "Vinai"
        self.user_agent = "user agent"
        self.created_at = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.updated_at = pytz.utc.localize(datetime.datetime(2017, 6, 3, 0, 0))
        self.model = Analytics.objects.create(ip_address=self.ip_address, referrer=self.referrer,
                                              user_agent=self.user_agent, created_at=self.created_at,
                                              updated_at=self.updated_at)
        self.model.save()
        self.attributes = ["ip_address", "referrer", "user_agent", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "Ryan"
        self.parent = None
