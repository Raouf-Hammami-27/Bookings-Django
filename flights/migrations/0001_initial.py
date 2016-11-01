# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=255)),
                ('depart', models.DateField()),
                ('arrivee', models.DateField()),
                ('origine', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('modele', models.CharField(max_length=255)),
            ],
        ),
    ]
