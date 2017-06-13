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
        self.created_at = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))
        self.updated_at = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))
        self.model = Analytics.objects.create(ip_address=self.ip_address, referrer=self.referrer,
                                              user_agent=self.user_agent, created_at=self.created_at,
                                              updated_at=self.updated_at)
        self.model.save()
        self.attributes = ["ip_address", "referrer",
                           "user_agent", "created_at", "updated_at"]
        self.model_update_index = 1
        self.model_update_input = "Ryan"
        self.parent = None
        self.ip_address2 = "127.94.0.3"
        self.model_second = Analytics.objects.create(ip_address=self.ip_address, referrer="Ryan",
                                                     user_agent=self.user_agent, created_at=self.created_at,
                                                     updated_at=self.updated_at)
        self.model_third = Analytics.objects.create(ip_address=self.ip_address2, referrer="Ryan",
                                                    user_agent=self.user_agent, created_at=self.created_at,
                                                    updated_at=self.updated_at)

    def test_hits_by_ip(self):
        # testing search
        models = list(Analytics.hits_by_ip(self.ip_address))
        self.assertEqual(len(models), 2)
        model_first, model_second = models[0], models[1]
        # testing desc
        self.assertEqual(model_first, self.model_second)
        self.assertEqual(model_second, self.model)
        # testing search with different ip
        model_third = Analytics.hits_by_ip(self.ip_address2)[0]
        self.assertEqual(model_third, self.model_third)
        # testing with col specified
        models2 = list(Analytics.hits_by_ip(self.ip_address, 'referrer'))
        self.assertEqual(len(models2), 2)

    def test_count_by_col(self):
        count1 = Analytics.count_by_col('referrer')
        self.assertEqual(count1, 3)
        count2 = Analytics.count_by_col('created_at')
        self.assertEqual(count2, 3)

    def test_parse_field(self):
        valid_fields = ["ip_address", "referrer", "user_agent"]
        invalid_fields = ["password", "id", "admin"]
        for field in valid_fields:
            self.assertEqual(field, Analytics.parse_field(field))
        for field in invalid_fields:
            self.assertEqual("1", Analytics.parse_field(field))
