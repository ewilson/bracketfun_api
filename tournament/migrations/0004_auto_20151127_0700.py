# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20151127_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pool',
            field=models.CharField(default='', max_length=1, blank=True),
        ),
    ]
