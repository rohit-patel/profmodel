# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-21 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0008_auto_20170420_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactiondata',
            old_name='Department',
            new_name='BusinessUnit',
        ),
    ]