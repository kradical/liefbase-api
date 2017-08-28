# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reliefmap',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='relief_maps', to=settings.AUTH_USER_MODEL),
        ),
    ]