# Generated by Django 5.0.6 on 2024-06-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massages', '0007_messages_file_messages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/'),
        ),
    ]
