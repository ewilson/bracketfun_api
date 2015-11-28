# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('home_score', models.SmallIntegerField(default=0)),
                ('away_score', models.SmallIntegerField(default=0)),
                ('pool', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('state', models.SmallIntegerField(default=0, choices=[(0, 'Setup'), (1, 'Play'), (2, 'Complete')])),
                ('type', models.SmallIntegerField(default=0, choices=[(0, 'Round-robin'), (1, 'Pools')])),
                ('players', models.ManyToManyField(to='tournament.Player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='away_player',
            field=models.ForeignKey(related_name='away_matches', to='tournament.Player', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='match',
            name='home_player',
            field=models.ForeignKey(related_name='home_matches', to='tournament.Player', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(related_name='matches', to='tournament.Tournament'),
        ),
    ]
