from datetime import timedelta
from time import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    is_online = models.BooleanField(default=False)

    def update_online_status(self):
        if self.last_login:
            now = timezone.now()
            if now - self.last_login < timedelta(minutes=1):
                self.is_online = True
            else:
                self.is_online = False
        else:
            self.is_online = False
        self.save()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username






class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} "
