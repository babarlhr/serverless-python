# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20180220_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='Description1',
            field=models.CharField(blank=True, default='Description of above service', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Description2',
            field=models.CharField(blank=True, default='Description of above service', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Description3',
            field=models.CharField(blank=True, default='Description of above service', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Description4',
            field=models.CharField(blank=True, default='Description of above service', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Description5',
            field=models.CharField(blank=True, default='Description of above service', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Point1',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Point2',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Point3',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Point4',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='Point5',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
