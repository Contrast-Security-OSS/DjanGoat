# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils import timezone
from app.models import User, Message
from app.tests.mixins import ModelCrudTests, Pep8ModelTests


class MessageModelTests(TestCase, ModelCrudTests, Pep8ModelTests):
    # Setting up 2 testcases

    def setUp(self):
        # Create the sender
        input_email = "ryan.dens@example.com"
        input_password = "12345"
        input_admin = True
        input_first_name = "Ryan"
        input_last_name = "Dens"

        self.parent = User.objects.create(
            email=input_email, password=input_password,
            is_admin=input_admin, first_name=input_first_name,
            last_name=input_last_name, created_at=timezone.now(),
            updated_at=timezone.now()
        )

        # Create the receiver
        input_email_receiver = "galen.palmer@example.com"
        input_password_receiver = "12345"
        input_admin_receiver = True
        input_first_name_receiver = "Galen"
        input_last_name_receiver = "Palmer"

        receiver = User.objects.create(
            email=input_email_receiver, password=input_password_receiver,
            is_admin=input_admin_receiver, first_name=input_first_name_receiver,
            last_name=input_last_name_receiver, created_at=timezone.now(),
            updated_at=timezone.now()
        )

        # Create Message Model
        self.model = Message.objects.create(creator=self.parent, receiver=receiver,
                                            message="Hello", read=False,
                                            created_at=timezone.now(),
                                            updated_at=timezone.now())

        # Model attributes to be updated
        self.attributes = ["creator", "receiver",
                           "message", "read",
                           "created_at", "updated_at"]
        self.model_update_index = 2
        self.model_update_input = "Goodby"

        # Path for pep8 tests
        self.path = "app/models/Message/message.py"
