# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_extras', '0003_auto_20170614_2137'),
        ('website', '0010_auto_20170615_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='incentivemodel',
            name='user',
            field=models.ManyToManyField(blank=True, to='reg_extras.UserProfile'),
        ),
    ]
