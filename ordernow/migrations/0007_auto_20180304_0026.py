# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-03 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordernow', '0006_auto_20180304_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/'),
        ),
    ]
