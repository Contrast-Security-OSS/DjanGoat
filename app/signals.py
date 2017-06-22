from app.models import User, Pay
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def create_user_values(sender, instance, *args, **kwargs):
    if instance.pk is None:
        instance.generate_token()
        instance.hash_password()
        instance.assign_user_id()


@receiver(pre_save, sender=Pay)
def encrypt(sender, instance, *args, **kwargs):
    if instance.pk is None:
        instance.encrypt_bank_num()
