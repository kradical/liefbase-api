# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_mapitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapitem',
            old_name='location',
            new_name='point',
        ),
    ]