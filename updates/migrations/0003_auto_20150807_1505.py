# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0002_chirp_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='chirp',
            name='message',
            field=models.CharField(max_length=140, validators=[django.core.validators.MinLengthValidator(5, message='Type more than 5 characters lazy ass')]),
        ),
        migrations.AddField(
            model_name='tag',
            name='chirps',
            field=models.ManyToManyField(to='updates.Chirp'),
        ),
    ]
