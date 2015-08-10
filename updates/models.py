import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.utils import timezone


class Chirp(models.Model):
    author = models.ForeignKey(User)
    message = models.CharField(max_length=140,
                               validators=[MinLengthValidator(5, message="Type more than 5 characters lazy ass")])
    title = models.CharField(max_length=30)
    posted_at = models.DateTimeField()

    def was_published_recently(self):
        """
        Will return if the chirp was within 1 day
        :return:
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.posted_at <= now

    def __str__(self):
        return "{} by {} posted {}".format(self.title, self.author, self.title)

class Tag(models.Model):
    name = models.CharField(max_length=10)
    chirps = models.ManyToManyField(Chirp)

    def __str__(self):
        return self.name