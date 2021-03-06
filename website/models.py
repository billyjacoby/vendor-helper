# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from reg_extras.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.formats import dateformat
from django.utils import timezone

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
    date_added = models.DateTimeField(default=timezone.now, blank=False)
    company = models.ForeignKey('CompanyModel', blank=False)
    description = models.TextField(blank=False)
    payout = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    users_subscribed = models.ManyToManyField(User, blank=True, related_name='incentives_subscribed')
    contact_name = models.CharField(max_length=128, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            formatted_date = dateformat.format(self.end_date, "M-'y")
            name = '%s | %s' % (self.supplier, formatted_date)
            return name

class UserIncentiveModel(models.Model):
    incentivemodel = models.ForeignKey(IncentiveModel, blank=False)
    comments = models.TextField(blank=True)
    date_completed = models.DateField(blank=True)
    location = models.CharField(max_length=128, blank=True)
    completed = models.BooleanField(blank=False, default=False)
    payed = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey(User, blank=False)
    payout = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to="media/images/user_incentive_images/", blank=True )

    def save(self, *args, **kwargs):
        if not self.payout:
            self.payout = self.incentivemodel.payout
        super(UserIncentiveModel, self).save(*args, **kwargs)

    def __unicode__(self):
        if self.incentivemodel.name:
            return self.incentivemodel.name
        else:
            formatted_date = dateformat.format(self.incentivemodel.end_date, "M-'y")
            name = '%s | %s' % (self.incentivemodel.supplier, formatted_date)
            return name


class TaskModel(models.Model):
    name = models.CharField(max_length=128, blank=False)
    location = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now, blank=False)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, blank=False)

    def __unicode__(self):
        return self.name
