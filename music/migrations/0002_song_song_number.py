# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_number',
            field=models.IntegerField(default=0),
        ),
    ]
