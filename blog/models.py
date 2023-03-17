from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):      # dodane *args, **kwargs
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return self.title

