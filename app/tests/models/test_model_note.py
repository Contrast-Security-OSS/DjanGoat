# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from app.models import *

from django.utils import timezone


# Models Test
class ModelsTests(TestCase):
    def test_can_create_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())

        self.assertEquals(
            str(note),
            'Hey!',
        )
