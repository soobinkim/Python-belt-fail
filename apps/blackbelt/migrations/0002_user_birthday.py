# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbelt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
