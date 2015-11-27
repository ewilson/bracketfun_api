# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20151127_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='pool',
            field=models.CharField(default='', max_length=1),
        ),
    ]
