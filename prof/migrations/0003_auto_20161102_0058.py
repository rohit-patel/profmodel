# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_filespace'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filespace',
            options={'permissions': (('file_owner', 'File Owner'),)},
        ),
        migrations.RemoveField(
            model_name='filespace',
            name='Owner',
        ),
    ]
