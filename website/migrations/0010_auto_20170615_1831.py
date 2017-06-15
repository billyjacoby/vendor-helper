# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170614_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incentivemodel',
            name='company',
        ),
        migrations.AddField(
            model_name='incentivemodel',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='website.CompanyModel'),
            preserve_default=False,
        ),
    ]