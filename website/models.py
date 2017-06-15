# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CompanyModel(models.Model):
    name = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=False)
    image = models.ImageField(blank=True)
    email_domain = models.CharField(blank=True, max_length=128)

    def __unicode__(self):
        return self.name
