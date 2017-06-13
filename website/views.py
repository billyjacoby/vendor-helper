# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from reg_extras.forms import UserProfileRegistrationForm, EditUserProfileForm, EditUserForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    content = {}
    return render(request, 'website/index.html', content)

def about(request):
    content = {}
    return render(request, 'website/about.html', content)

def contact(request):
    content = {}
    return render(request, 'website/contact.html', content)

@login_required
def view_profile(request):
    profile = request.user.get_username()
    content = {
    "profile":profile,
    }
    return render(request, 'website/view_profile.html', content)

@login_required
def edit_profile(request):
    content = {}
    profile = request.user.get_username()
    if request.method == 'POST':
        form = EditUserProfileForm (request.POST, instance=request.user.userprofile)
        form2 = EditUserForm (request.POST, instance=request.user)
        content['form'] = form
        content['form2'] = form2

        #if form.is_valid() and form2.is_valid():
        if form2.is_valid():
            new_user = form.save()
            new_user2 = form2.save()
            return render(request, 'website/view_profile.html', content)

        else:
            content['form.errors'] = form.errors
            content['form2.errors'] = form2.errors
    else:
        form = EditUserProfileForm(instance=request.user.userprofile)
        form2 = EditUserForm(instance=request.user)
        content['form']= form
        content['form2'] = form2
    return render(request, 'website/edit_profile.html', content)
