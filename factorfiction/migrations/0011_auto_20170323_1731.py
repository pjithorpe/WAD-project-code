# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factorfiction', '0010_auto_20170323_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='profile_images/default.png', upload_to='profile_images'),
        ),
    ]