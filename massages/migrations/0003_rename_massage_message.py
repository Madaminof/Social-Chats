# Generated by Django 5.0.6 on 2024-06-12 13:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('massages', '0002_remove_massage_user_massage_recipient_massage_sender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Massage',
            new_name='Message',
        ),
    ]