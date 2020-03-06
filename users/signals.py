from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile

# signals is created, so that every time a user is created, signals fire to automatically create a Profile

@receiver(post_save, sender=User)
# we pass sender(User model), the instance (instance of new user), if user is created(boolean)
def create_and_save_profile(sender, instance, created, **kwargs):
    if created:
        print("MD log: New User has been created, making profile...")
        Profile.objects.create(user=instance)
        print("MD log: profile created, saving...")
        instance.profile.save()
        print("MD log: profile saved")
