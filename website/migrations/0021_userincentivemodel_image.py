# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20170629_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='userincentivemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/user_incentive_images/'),
        ),
    ]