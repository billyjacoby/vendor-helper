# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# this is the first step in defining new fields for registration-redux
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    verified_email = models.BooleanField(blank=True, default = False)
    company_name = models.CharField(max_length=100, blank=True)
    company = models.ForeignKey('website.CompanyModel', blank=True, null=True)

    def __unicode__(self):
        return self.user.username
