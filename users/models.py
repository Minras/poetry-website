from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    MAX_IMG_SIZE = 512 # max allowed image width or height

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > self.MAX_IMG_SIZE or img.width>self.MAX_IMG_SIZE:
            output_size = (self.MAX_IMG_SIZE, self.MAX_IMG_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path )
