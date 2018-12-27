from django.db import models


class Twit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title


