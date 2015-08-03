from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chirp(models.Model):
    author = models.ForeignKey(User)
    message = models.CharField(max_length=140)
    title = models.CharField(max_length=10)
    posted_at = models.DateTimeField()