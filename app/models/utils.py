from app.models.KeyManagement.key_management import KeyManagement
from django.conf import settings
from Crypto.Cipher import AES


class Encryption():

    @staticmethod
    def encrypt_sensitive_value(user, value):
        aes = AES.new(Encryption.get_key(), AES.MODE_CBC, Encryption.get_iv(user))
        return aes.encrypt(Encryption.pad(value))

    @staticmethod
    def decrypt_sensitive_value(user, value):
        aes = AES.new(Encryption.get_key(), AES.MODE_CBC, Encryption.get_iv(user))
        return Encryption.unpad(aes.decrypt(value))

    @staticmethod
    def key_management(user):
        try:
            return KeyManagement.objects.get(user=user)
        except KeyManagement.DoesNotExist:
            raise Exception("User is not present")
        except KeyManagement.MultipleObjectsReturned:
            raise Exception("Users are sharing the same user_id")

    @staticmethod
    def get_iv(user):
        return Encryption.key_management(user).iv

    @staticmethod
    def get_key():
        key = settings.KEY
        if key is None:
            raise Exception('Key not specified in settings.py file')
        else:
            return key

    @staticmethod
    def pad(s):
        bs = 16
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]
