# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0039_auto_20181027_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='block',
            field=models.IntegerField(default=31),
            preserve_default=False,
        ),
    ]
