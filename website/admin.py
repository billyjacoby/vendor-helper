# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from website.models import CompanyModel, IncentiveModel, TaskModel, UserIncentiveModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(IncentiveModel)
admin.site.register(TaskModel)
