# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-18 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subject',
        ),
    ]