# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-30 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_auto_20170329_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filespace',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='filespace',
            old_name='file',
            new_name='File',
        ),
        migrations.RenameField(
            model_name='filespace',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='filespace',
            old_name='type',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='transactiondata',
            old_name='BusinessUnit',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='transactiondata',
            old_name='SourceFileObject',
            new_name='SourceFile',
        ),
        migrations.RenameField(
            model_name='transactiondata',
            old_name='TransactionDate',
            new_name='TransactionDate',
        ),
        migrations.RenameField(
            model_name='transactiondata',
            old_name='TransactionNumber',
            new_name='TransactionNumber',
        ),
    ]
