# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-05 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_auto_20180505_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='Linkedin_profile',
            field=models.CharField(default='', max_length=254),
        ),
    ]
