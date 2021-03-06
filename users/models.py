from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username} profile"

    # Override models save method
    def save(self):
        super().save()  # Call parent save method

        img = Image.open(self.image.path)  # Get saved image

        if img.height > 300 or img.width > 300:
            desired_size = (300, 300)
            img.thumbnail(desired_size)
            img.save(self.image.path)
