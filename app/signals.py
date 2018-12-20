# Django imports
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Local imports
from app.models import User, Pay


@receiver(pre_save, sender=User)
def create_user_values(sender, instance, *args, **kwargs):  # pylint: disable=unused-argument
    if instance.pk is None:
        instance.generate_token()
        instance.assign_user_id()
    instance.hash_password()


@receiver(pre_save, sender=Pay)
def encrypt(sender, instance, *args, **kwargs):  # pylint: disable=unused-argument
    if instance.pk is None:
        instance.encrypt_bank_num()
