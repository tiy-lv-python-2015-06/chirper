import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Manager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class JeffChirpsManager(Manager):
    def get_queryset(self):
        return super(JeffChirpsManager, self).get_queryset().filter(author__username='jeff')


class Chirp(models.Model):

    author = models.ForeignKey(User)
    message = models.CharField(max_length=140,
                               validators=[MinLengthValidator(5, message="Type more than 5 characters lazy ass")])
    title = models.CharField(max_length=30)
    posted_at = models.DateTimeField(auto_now_add=True)
    #modified_at = models.DateTimeField(auto_now=True)

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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        print("New User Created")