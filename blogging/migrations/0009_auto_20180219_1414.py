# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0008_auto_20180219_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='blog/'),
        ),
    ]
