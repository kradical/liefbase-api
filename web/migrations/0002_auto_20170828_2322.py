# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-28 23:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='users',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]