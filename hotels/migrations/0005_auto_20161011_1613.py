# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_hotel_etoiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='actif',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='date_creation',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='notes',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='ville',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
