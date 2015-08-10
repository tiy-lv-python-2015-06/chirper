# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20150810_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
