# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20150820_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('age', models.IntegerField(blank=True, default=18, help_text='Your age unless you lie')),
                ('zip', models.IntegerField(blank=True, db_index=True, verbose_name='Zip Code', null=True)),
                ('salary', models.DecimalField(max_digits=9, decimal_places=2)),
                ('relationship', models.CharField(max_length=2, choices=[('C', 'Complicated'), ('R', 'In a relationship'), ('S', 'Single')], default='S', verbose_name='Relationship Status')),
                ('photo', models.ImageField(blank=True, upload_to='avatars', null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
