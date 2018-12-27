from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    pic = models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')

