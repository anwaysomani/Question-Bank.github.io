# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-18 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0005_auto_20181018_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='branch',
        ),
    ]