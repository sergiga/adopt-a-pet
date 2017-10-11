# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_adoptionstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='adoptions', to='pets.AdoptionStatus'),
        ),
    ]