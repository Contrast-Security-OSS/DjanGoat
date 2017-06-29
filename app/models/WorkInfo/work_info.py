# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from django.db import models

# local imports
from app.models.utils import Encryption


@python_2_unicode_compatible
class WorkInfo(models.Model):
    """
    Class defining the WorkInfo model

    t.integer  "user_id",       limit: 4
    t.string   "income",        limit: 255
    t.string   "bonuses",       limit: 255
    t.integer  "years_worked",  limit: 4
    t.string   "SSN",           limit: 255
    t.date     "DoB"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.binary   "encrypted_ssn", limit: 65535
    """
    MAX_INT_VALUE = 2 ** 32 - 1

    def __str__(self):
        return self.user.__str__() + " WorkInfo Summary: \n" \
               + "\nIncome: " + str(self.income) \
               + "\nBonuses: " + str(self.bonuses) \
               + "\nYears Worked: " + str(self.years_worked) \
               + "\nSSN: " + str(self.SSN) \
               + "\nDate of Birth: " + str(self.DoB)

    user = models.ForeignKey('User', on_delete=models.CASCADE,
                             related_name="work_info")
    income = models.CharField(max_length=255)
    bonuses = models.CharField(max_length=255)
    years_worked = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_INT_VALUE)]
    )
    SSN = models.CharField(max_length=255)
    DoB = models.DateField('DoB')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    encrypted_ssn = models.BinaryField()

    def encrypt_ssn(self):
        self.encrypted_ssn = Encryption.encrypt_sensitive_value(
            self.user, self.SSN
        )
        self.SSN = None

    def decrypt_ssn(self):
        return Encryption.decrypt_sensitive_value(
            self.user, self.encrypted_ssn
        )

    def income_to_int(self):
        return int(self.income[1:].replace(',', ''))

    class Meta:
        db_table = "app_work_infos"
