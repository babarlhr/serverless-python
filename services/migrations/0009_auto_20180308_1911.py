# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-08 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_servicemodel_description_long'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicemodel',
            options={'ordering': ['-updated', 'timestamp']},
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]