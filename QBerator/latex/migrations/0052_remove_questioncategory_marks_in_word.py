# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0051_questioncategory_marks_in_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioncategory',
            name='marks_in_word',
        ),
    ]