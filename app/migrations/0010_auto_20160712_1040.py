# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 02:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160712_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 40, 29, 429713), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 40, 29, 430219), null=True),
        ),
    ]
