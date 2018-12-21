from django.db import models


class Twit(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
