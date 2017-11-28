# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

from app.models import Note
from app.tests.mixins import Pep8ModelTests


class NoteModelTests(TestCase, Pep8ModelTests):
    def setUp(self):
        self.path = "app/models/Note/note.py"

    def test_can_create_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())

        self.assertEquals(str(note), 'Hey!')

    def test_can_read_note(self):
        note = Note(note_name="Hey!", pub_date=timezone.now())
        self.assertEquals(note.id, None)
        note.save()
        self.assertNotEquals(note.id, None)
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
        Note.objects.get(note_name="Hey!").delete()
        self.assertEquals(0, len(Note.objects.all()))
