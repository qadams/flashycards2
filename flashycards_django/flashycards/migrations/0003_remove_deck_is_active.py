# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashycards', '0002_deck_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='is_active',
        ),
    ]
