# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, RequestFactory, Client

from app.models import Note

from django.utils import timezone


# Models Test
class ModelsTests(TestCase):
    def test_can_create_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())

        self.assertEquals(str(note), 'Hey!')

    def test_can_read_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())
        note.save()
        retrieved = Note.objects.get(note_name="Hey!")
        self.assertEquals("Hey!", retrieved.note_name)

    def test_can_update_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())
        note.save()
        note.note_name = "Vinai!"
        note.save()
        note2 = Note(note_name="Yo!", pub_date=timezone.now())
        note2.save()
        self.assertEquals(2, len(Note.objects.all()))
        self.assertEquals("Vinai!", Note.objects.get(note_name="Vinai!").note_name)

    def test_can_delete_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())
        note.save()
        p = Note.objects.get(note_name="Hey!").delete()
        self.assertEquals(0, len(Note.objects.all()))
