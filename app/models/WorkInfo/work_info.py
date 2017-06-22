# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator
from Crypto.Cipher import AES
from django.conf import settings
from app.models.KeyManagement.key_management import KeyManagement

KEY = settings.KEY


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

    def key_management(self):
        try:
            return KeyManagement.objects.get(user=self.user)
        except KeyManagement.DoesNotExist:
            raise Exception("User is not present")
        except KeyManagement.MultipleObjectsReturned:
            raise Exception("Users are sharing the same user_id")

    def get_iv(self):
        if self.key_management().iv is None:
            raise Exception('A iv value was not specified')
        else:
            return self.key_management().iv

    def get_key(self):
        if KEY is None:
            raise Exception('Key not specified in settings.py file')
        else:
            return KEY

    @staticmethod
    def pad(s):
        bs = 16
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt_ssn(self):
        aes = AES.new(self.get_key(), AES.MODE_CBC, self.get_iv())
        self.encrypted_ssn = aes.encrypt(self.pad(self.SSN))
        self.SSN = None

    def decrypt_ssn(self):
        aes = AES.new(self.get_key(), AES.MODE_CBC, self.get_iv())

        return self.unpad(aes.decrypt(self.encrypted_ssn))

    class Meta:
        db_table = "app_work_infos"
