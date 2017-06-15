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

class IncentiveModel(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    supplier = models.CharField(max_length=128, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    company = models.ForeignKey('CompanyModel', blank=False)
    description = models.TextField(blank=False)
    payout = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            name = '%s - %s' % (self.supplier, self.start_date)
            return name
