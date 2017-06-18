# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from reg_extras.forms import UserProfileRegistrationForm, EditUserProfileForm, EditUserForm
from django.contrib.auth.models import User

from datetime import date, timedelta, datetime

from website.models import IncentiveModel
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

@login_required
def incentive_detail(request, incentive_pk):
    incentive = get_object_or_404(IncentiveModel, pk=incentive_pk)
    content = {}
    content['incentive'] = incentive
    subscribed= False
    if request.user in incentive.users_subscribed.all():
        subscribed = True
    content['subscribed'] = subscribed
    return render(request, 'website/incentive_detail.html', content)

@login_required
def user_dashboard(request):
    content = {}
    content['incentive_by_date'] = IncentiveModel.objects.order_by('-date_added')[:5]

    username=request.user.id
    content['subscribed_incentives'] = IncentiveModel.objects.filter(users_subscribed__id=username)

    five_days = date.today() + timedelta(days=7)
    content['five_days'] = five_days
    content['tasks_due_soon'] = IncentiveModel.objects.filter(end_date__range=[date.today(), five_days])

    return render(request, 'website/user_dashboard.html', content)

@login_required
def manage_incentive_subscription(request, incentive_pk):
    incentive = get_object_or_404(IncentiveModel, pk=incentive_pk)
    content = {}
    if request.user in incentive.users_subscribed.all():
        incentive.users_subscribed.remove(request.user)
    else:
        incentive.users_subscribed.add(request.user)
    return redirect("incentive_detail", incentive_pk=incentive_pk)

@login_required
def incentive_list(request):
    content = {}
    content['incentive_list'] = IncentiveModel.objects.all().order_by('end_date')
    return render(request, 'website/incentive_list.html', content)
