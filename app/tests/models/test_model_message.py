# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from app.models import Message
from django.utils import timezone

# Create your tests here.

class MessageModelTests(TestCase):
    # Setting up 2 testcases
    def setUp(self):
        Message.objects.create(creator_id = 1, receiver_id = 2, message = "hello", read = False,
                               created_at = timezone.now(), updated_at = timezone.now())
        Message.objects.create(creator_id = 3, receiver_id = 4, message = "hi", read = True,
                               created_at=timezone.now(), updated_at=timezone.now())


    # Testing create models
    def test_create(self):
        M1 = Message.objects.get(creator_id = 1)
        self.assertNotEqual(M1, None)
        M2 = Message.objects.get(creator_id = 3)
        self.assertNotEqual(M2, None)

    # Testing read models
    def test_read(self):
        #Testing type, value of first message
        M1 = Message.objects.get(creator_id = 1)
        self.assertEqual(M1.creator_id, 1)
        self.assertEqual(M1.receiver_id, 2)
        self.assertEqual(M1.message, "hello")
        self.assertEqual(M1.read, False)

        M2 = Message.objects.get(creator_id = 3)
        self.assertEqual(M2.creator_id, 3)
        self.assertEqual(M2.receiver_id, 4)
        self.assertEqual(M2.message, "hi")
        self.assertEqual(M2.read, True)

    # Testing update models
    def test_update(self):
        M1 = Message.objects.get(creator_id = 1)
        M1.receiver_id = 5
        M1.save()
        R1 = Message.objects.get(creator_id = 1)
        self.assertEqual(R1.receiver_id, 5)

        M2 = Message.objects.get(creator_id = 3)
        M2.message = "changed"
        M2.save()
        R2 = Message.objects.get(creator_id = 3)
        self.assertEqual(R2.message, "changed")

    # Testing delete models
    def test_delete(self):
        M = Message.objects.all()
        self.assertEqual(len(M), 2)

        M1 = Message.objects.get(creator_id = 1)
        M1.delete()
        M = Message.objects.all()
        self.assertEqual(len(M), 1)

        M2 = Message.objects.get(creator_id = 3)
        M2.delete()
        M = Message.objects.all()
        self.assertEqual(len(M), 0)
