from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    pic = models.ImageField(upload_to='pic_folder/')
    ke = models.CharField(max_length=1000)
