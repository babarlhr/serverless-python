# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordernow', '0002_auto_20180221_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]