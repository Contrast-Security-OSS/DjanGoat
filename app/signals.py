from app.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def create_user_values(sender, instance, *args, **kwargs):
    instance.assign_user_id()
    instance.generate_token()
    instance.hash_password()
