# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factorfiction', '0005_uservotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='totalVotes',
            field=models.IntegerField(default=0),
        ),
    ]