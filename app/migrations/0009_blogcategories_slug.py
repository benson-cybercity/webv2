# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170208_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategories',
            name='slug',
            field=models.SlugField(default='engineering'),
            preserve_default=False,
        ),
    ]
