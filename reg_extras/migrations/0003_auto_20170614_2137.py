# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg_extras', '0002_userprofile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.CompanyModel'),
        ),
    ]
