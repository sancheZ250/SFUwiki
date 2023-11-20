from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    reputation = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='user_avatars', null=True, blank=True)

    def __str__(self):
        return self.user.username