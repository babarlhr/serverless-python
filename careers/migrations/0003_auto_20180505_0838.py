# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-05 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0002_auto_20180505_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careermodel',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]