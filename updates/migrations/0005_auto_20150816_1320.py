# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0004_auto_20150810_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
