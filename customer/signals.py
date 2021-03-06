from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from customer.models import Customer

User = get_user_model()


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, email=instance.email)


@receiver(pre_save, sender=Customer)
def update_customer_state(sender, instance, **kwargs):
    if not instance._state.adding:
        instance.is_registered = False


@receiver(pre_save, sender=User)
def unique_username(sender, instance, **kwargs):
    instance.username = instance.email
