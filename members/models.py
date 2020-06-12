import os
from django.contrib.auth.models import User
from django.db import models

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to='media/')

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/media/default.jpeg"

    def __str__(self):
        return self.user.username