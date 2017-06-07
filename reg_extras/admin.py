# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# added for first and last name
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from reg_extras.models import UserProfile
# Register your models here.


# Register your models here.
admin.site.unregister(User)
class UserProfileInine(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInine, ]
admin.site.register(User, UserProfileAdmin)
