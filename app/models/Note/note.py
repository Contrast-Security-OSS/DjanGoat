from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Sample Note model


@python_2_unicode_compatible
class Note(models.Model):
    def __str__(self):
        return self.note_name

    note_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        db_table = "app_notes"
