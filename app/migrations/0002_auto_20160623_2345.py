# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-23 15:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 23, 23, 45, 44, 472835), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 23, 23, 45, 44, 473403), null=True),
        ),
    ]
