# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 19:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0011_incentivemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incentivemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='incentivemodel',
            name='users_subscribed',
            field=models.ManyToManyField(blank=True, related_name='incentives_subscribed', to=settings.AUTH_USER_MODEL),
        ),
    ]
