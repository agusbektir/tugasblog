import os
from django.contrib.auth.models import User
from django.db import models


def photo_path(instance, filename):
    return os.path.join('prof_pic', instance.user.username, filename)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to=photo_path)

    def __str__(self):
        return self.user.username