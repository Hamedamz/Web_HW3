from django.db import models
from django.contrib.auth.models import User
import uuid


class Sess(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True)

    def generateAnotherKey(self):
        self.uid=uuid.uuid4()
