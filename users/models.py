from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# imported the User for One to One relationship
# used models.OneToOneField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    header = models.CharField(max_length=255, blank=True)
    about_me = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
