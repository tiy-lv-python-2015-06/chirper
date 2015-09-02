from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    COMPLICATED = 'C'
    IN_RELATIONSHIP = 'R'
    SINGLE = 'S'
    RELATIONSHIP_STATUS_CHOICES = (
        (COMPLICATED, 'Complicated'),
        (IN_RELATIONSHIP, 'In a relationship'),
        (SINGLE, 'Single')
    )

    user = models.OneToOneField(User, null=True)
    age = models.IntegerField(blank=True, default=18, help_text='Your age unless you lie')
    zip = models.IntegerField(null=True, blank=True, db_index=True, verbose_name='Zip Code')
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    relationship = models.CharField(max_length=2, choices=RELATIONSHIP_STATUS_CHOICES,
                                    default=SINGLE, verbose_name='Relationship Status')
    photo = models.ImageField(upload_to="avatars", blank=True, null=True)



