# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20160203_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='property',
            new_name='assoc_property',
        ),
        migrations.AddField(
            model_name='assessment',
            name='assoc_property',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='property.Property'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='assoc_property',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='property.Property'),
            preserve_default=False,
        ),
    ]
