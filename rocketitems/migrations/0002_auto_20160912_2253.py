# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rocketitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='variationattribute',
            unique_together=set([('variation', 'attribute')]),
        ),
    ]