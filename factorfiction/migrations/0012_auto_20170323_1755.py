# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 17:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factorfiction', '0011_auto_20170323_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservotes',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factorfiction.Page'),
        ),
        migrations.AlterField(
            model_name='uservotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
