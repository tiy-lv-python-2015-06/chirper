# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='title',
            field=models.CharField(default='N/A', max_length=10),
            preserve_default=False,
        ),
    ]
