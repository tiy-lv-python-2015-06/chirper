from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    age = models.IntegerField()
    zip = models.IntegerField()
