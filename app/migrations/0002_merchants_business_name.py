# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchants',
            name='business_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
