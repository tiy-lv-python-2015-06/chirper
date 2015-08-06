import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Chirp(models.Model):
    author = models.ForeignKey(User)
    message = models.CharField(max_length=140)
    title = models.CharField(max_length=10)
    posted_at = models.DateTimeField()

    def was_published_recently(self):
        """
        Was this published in the last 30 days
        :return:
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.posted_at <= now


    def __str__(self):
        return "{} by {} posted {}".format(self.title, self.author, self.title)