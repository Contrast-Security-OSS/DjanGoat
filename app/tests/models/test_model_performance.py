# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import datetime
import pytz
from app.models import User
from app.models import Performance
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class PerformanceModelTests(TestCase, ModelCrudTests, Pep8ModelTests):

    def setUp(self):

        # Create the user
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"
        u_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 1, 0, 0))
        u_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 3, 0, 0))

        self.parent = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=u_input_create_date,
            updated_at=u_input_update_date
        )

        # Create the Reviewer
        input_email_reviewer = "ziyang.wang@example.com"
        input_password_reviewer = "12345"
        input_admin_reviewer = True
        input_first_name_reviewer = "Ziyang"
        input_last_name_reviewer = "Wang"
        u_input_create_date_reviewer = pytz.utc.localize(
            datetime.datetime(2017, 4, 1, 0, 0))
        u_input_update_date_reviewer = pytz.utc.localize(
            datetime.datetime(2017, 5, 3, 0, 0))

        user_reviewer = User.objects.create(
            email=input_email_reviewer, password=input_password_reviewer,
            is_admin=input_admin_reviewer, first_name=input_first_name_reviewer,
            last_name=input_last_name_reviewer, created_at=u_input_create_date_reviewer,
            updated_at=u_input_update_date_reviewer
        )

        # Create Performance Model
        input_date_submitted = datetime.date(2017, 4, 6)
        input_score = 9
        input_comments = "123456789"
        perf_input_create_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 4, 0, 0))
        perf_input_update_date = pytz.utc.localize(
            datetime.datetime(2017, 6, 5, 0, 0))

        self.model = Performance.objects.create(
            date_submitted=input_date_submitted,
            score=input_score,
            comments=input_comments,
            created_at=perf_input_create_date,
            updated_at=perf_input_update_date,
            user=self.parent,
            reviewer=user_reviewer
        )

        # Model attributes to be updated
        self.attributes = ["user", "reviewer", "date_submitted", "score",
                           "comments", "created_at", "updated_at"]
        self.model_update_index = 3
        self.model_update_input = 10

        # Path for pep8 tests
        self.path = "app/models/Performance/performance.py"

    def test_reviewer_name(self):
        reviewer = User.objects.get(user_id=self.model.reviewer.user_id)
        performance_first = Performance.objects.get(reviewer=reviewer)
        self.assertEqual(performance_first.reviewer_name(),
                         "Ziyang Wang")
        reviewer.delete()
        self.assertEqual(performance_first.reviewer_name(), None)
