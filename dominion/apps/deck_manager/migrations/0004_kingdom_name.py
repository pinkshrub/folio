# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-27 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck_manager', '0003_auto_20160825_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='kingdom',
            name='name',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
    ]
