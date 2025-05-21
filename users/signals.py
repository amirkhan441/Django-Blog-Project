# Create the User signals for automatic profile creation

from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os
from django.conf import settings
from PIL import Image


def ensure_default_image_exists():
    default_path = os.path.join(settings.MEDIA_ROOT, 'default.jpg')
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    
    if not os.path.exists(default_path):
        
        img = Image.new('RGB', (300, 300), color = (73, 109, 137))
        img.save(default_path)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        
        ensure_default_image_exists()
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()