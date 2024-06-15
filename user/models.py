from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='media/images/',blank=True,null=True)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username



class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    image = models.ImageField(upload_to='media/images/', blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} "