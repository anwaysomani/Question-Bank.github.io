# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0032_auto_20181023_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='block',
            field=models.IntegerField(blank=True, default=27),
            preserve_default=False,
        ),
    ]
