from django.db.models.signals import post_save  # Fired after object is saved
from django.contrib.auth.models import User     # Sender: sends the signal
from django.dispatch import receiver            # Receiver: function gets signal and performs task
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
