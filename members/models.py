import os
from django.contrib.auth.models import User
from django.db import models

def photo_path(instance, filename):
    return os.path.join('member_pic', instance.user.username, filename)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to=photo_path)

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "media/default.jpeg"

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.user.username