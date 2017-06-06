# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
