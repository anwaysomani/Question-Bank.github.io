# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-25 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0004_auto_20180825_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_code',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
