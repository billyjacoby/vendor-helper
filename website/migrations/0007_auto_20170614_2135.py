# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_companymodel_email_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='email_domain',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
