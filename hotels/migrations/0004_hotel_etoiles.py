# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20161011_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='etoiles',
            field=models.PositiveIntegerField(default=4),
        ),
    ]