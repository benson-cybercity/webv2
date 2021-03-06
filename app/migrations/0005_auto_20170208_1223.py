# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 12:23
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_blogcategories_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Documentation',
                'verbose_name_plural': 'Documentations',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('decription', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='documentation',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tags'),
        ),
    ]
