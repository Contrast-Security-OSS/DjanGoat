# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from app.models import User, Message
from django.utils import timezone

# Create your tests here.


class MessageModelTests(TestCase):
    # Setting up 2 testcases

    def setUp(self):
        User.objects.create(email="ziyang.wang@contrastsecurity.com",
                            password="12345",
                            is_admin=True, first_name="Ziyang",
                            last_name="Wang", user_id=1,
                            created_at=timezone.now(), updated_at=timezone.now(),
                            auth_token="")
        Message.objects.create(creator_id=1, receiver_id=2, message="hello", read=False,
                               created_at=timezone.now(), updated_at=timezone.now())
        Message.objects.create(creator_id=3, receiver_id=4, message="hi", read=True,
                               created_at=timezone.now(), updated_at=timezone.now())

    # Testing creator_name method
    def test_creator_name(self):
        message_first = Message.objects.get(creator_id=1)
        self.assertEqual(message_first.creator_name(), "Ziyang Wang")
        message_second = Message.objects.get(creator_id=3)
        self.assertEqual(message_second.creator_name(),
                         "<b>Name unavailable</b>")

    # Testing create models
    def test_create(self):
        message_first = Message.objects.get(creator_id=1)
        self.assertNotEqual(message_first, None)
        message_second = Message.objects.get(creator_id=3)
        self.assertNotEqual(message_second, None)

    # Testing read models
    def test_read(self):
        # Testing type, value of first message
        message_first = Message.objects.get(creator_id=1)
        self.assertEqual(message_first.creator_id, 1)
        self.assertEqual(message_first.receiver_id, 2)
        self.assertEqual(message_first.message, "hello")
        self.assertEqual(message_first.read, False)

        message_second = Message.objects.get(creator_id=3)
        self.assertEqual(message_second.creator_id, 3)
        self.assertEqual(message_second.receiver_id, 4)
        self.assertEqual(message_second.message, "hi")
        self.assertEqual(message_second.read, True)

    # Testing update models
    def test_update(self):
        message_first = Message.objects.get(creator_id=1)
        message_first.receiver_id = 5
        message_first.save()
        receiver_first = Message.objects.get(creator_id=1)
        self.assertEqual(receiver_first.receiver_id, 5)

        message_second = Message.objects.get(creator_id=3)
        message_second.message = "changed"
        message_second.save()
        receiver_second = Message.objects.get(creator_id=3)
        self.assertEqual(receiver_second.message, "changed")

    # Testing delete models
    def test_delete(self):
        messages = Message.objects.all()
        self.assertEqual(len(messages), 2)

        message_first = Message.objects.get(creator_id=1)
        message_first.delete()
        messages = Message.objects.all()
        self.assertEqual(len(messages), 1)

        message_second = Message.objects.get(creator_id=3)
        message_second.delete()
        messages = Message.objects.all()
        self.assertEqual(len(messages), 0)
