# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_userincentivemodel_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='incentivemodel',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='incentivemodel',
            name='contact_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='userincentivemodel',
            name='payout',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]