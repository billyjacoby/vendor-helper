# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_companymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymodel',
            name='email_domain',
            field=models.URLField(blank=True, max_length=128),
        ),
    ]