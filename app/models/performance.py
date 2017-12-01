# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Performance(models.Model):
    """
    Class defining the Performance model

    t.integer  "user_id",        limit: 4
    t.date     "date_submitted"
    t.integer  "score",          limit: 4
    t.string   "comments",       limit: 255
    t.integer  "reviewer",       limit: 4
    t.datetime "created_at"
    t.datetime "updated_at"
    """
    MAX_INT_VALUE = 2 ** 32 - 1

    def __str__(self):
        return self.user.__str__() + " Performance Summary: \n" \
               + "\nReviewer: " + str(self.reviewer) \
               + "\nDate Submitted: " + str(self.date_submitted) \
               + "\nScore: " + str(self.score) + "\nComments: " + self.comments

    user = models.ForeignKey('User', related_name="u_id",
                             on_delete=models.CASCADE)
    reviewer = models.ForeignKey('User', related_name="r_id")
    date_submitted = models.DateField('date submitted')
    score = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    comments = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # returns the date as a string for proper chart formatting in the template
    def date_for_chart(self):
        return self.date_submitted.isoformat()

    class Meta:
        db_table = "app_performances"

    def reviewer_name(self):
        reviewer = self.user.__class__.objects.filter(
            user_id=self.reviewer.user_id
        ).first()
        if reviewer is not None:
            return reviewer.full_name()
        else:
            return None
