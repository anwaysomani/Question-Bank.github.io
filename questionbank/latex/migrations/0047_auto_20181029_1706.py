# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0046_questioncategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questioncategory',
            old_name='max_10mk',
            new_name='maximum_10mk',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='max_2mk',
            new_name='maximum_2mk',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='max_5mk',
            new_name='maximum_5mk',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='req_10mk',
            new_name='required_10mk',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='req_2mk',
            new_name='required_5mk',
        ),
        migrations.RenameField(
            model_name='questioncategory',
            old_name='req_5mk',
            new_name='requried_2mk',
        ),
    ]