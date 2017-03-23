# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factorfiction', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='', max_length=128),
        ),
    ]
