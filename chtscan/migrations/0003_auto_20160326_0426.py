# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chtscan', '0002_auto_20160323_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='end',
        ),
        migrations.AlterField(
            model_name='assessment',
            name='start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ON START'),
        ),
    ]
