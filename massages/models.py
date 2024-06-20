from django.db import models
from user.models import User


class Messages(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    video = models.FileField(upload_to='media/videos/', blank=True, null=True)
    file = models.FileField(upload_to='media/files', blank=True, null=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} - {self.sent_time}'

