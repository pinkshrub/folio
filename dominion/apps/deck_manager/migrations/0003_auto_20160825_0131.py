# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deck_manager', '0002_auto_20160825_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='creator',
            new_name='player',
        ),
        migrations.AddField(
            model_name='rating',
            name='card',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='deck_manager.Card'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='kingdom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='deck_manager.Kingdom'),
            preserve_default=False,
        ),
    ]
