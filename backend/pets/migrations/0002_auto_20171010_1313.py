# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='animal_type',
            new_name='pet_type',
        ),
    ]
