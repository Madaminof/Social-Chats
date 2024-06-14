from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
