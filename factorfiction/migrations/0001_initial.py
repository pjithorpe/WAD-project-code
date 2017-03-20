# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=5000)),
                ('answer', models.CharField(max_length=7)),
                ('fact', models.IntegerField(default=0)),
                ('fiction', models.IntegerField(default=0)),
                ('picture', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'GameArticles',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(default=' ')),
                ('postedBy', models.CharField(default='admin', max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('articleImage', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('facts', models.IntegerField(default=0)),
                ('fictions', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'pages',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('website', models.URLField(blank=True)),
                ('age', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
