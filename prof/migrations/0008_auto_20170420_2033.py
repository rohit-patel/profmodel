# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-21 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0007_auto_20170418_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='runspace',
            name='RunPeriodEnd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='runspace',
            name='RunPeriodStart',
            field=models.DateField(blank=True, null=True),
        ),
    ]
