from django.db import models


class Report(models.Model):
    remote_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now_add=True)

