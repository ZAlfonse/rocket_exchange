# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-17 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockettrade', '0002_auto_20170117_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingitem',
            name='value',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
