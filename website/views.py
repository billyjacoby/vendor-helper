# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from reg_extras.forms import UserProfileRegistrationForm, EditUserProfileForm, EditUserForm
from website.forms import TaskModelForm
from django.contrib.auth.models import User

from datetime import date, timedelta, datetime

from website.models import IncentiveModel, TaskModel
# Create your views here.
def index(request):
    content = {}
    return render(request, 'website/index.html', content)

def about(request):
    content = {}
    return render(request, 'website/about.html', content)

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
    content['subscribed_incentives'] = IncentiveModel.objects.filter(users_subscribed__id=username).order_by('end_date')

    five_days = date.today() + timedelta(days=7)
    content['five_days'] = five_days
    content['incentives_due_soon'] = IncentiveModel.objects.filter(end_date__range=[date.today(), five_days]).order_by('end_date')

    content['users_tasks'] = TaskModel.objects.filter(owner=request.user).filter(completed=False).order_by('due_date')[:3]

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

@login_required
def create_task(request):
    content = {}
    #instance = TaskModel(owner=request.user)
    #form = TaskModelForm(instance=instance)
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        content['form'] = form
        if form.is_valid():
            # idk how the fuck this worked, but it did...
            stock = form.save(commit=False)
            stock.owner = request.user
            stock.save()
            return redirect('user_dashboard')
        else:
            content['form.errors'] = form.errors
    else:
        form = TaskModelForm()
        content['form'] = form
    return render(request, 'website/create_task.html', content)

@login_required
def task_menu(request):
    content = {}

    user_tasks = TaskModel.objects.filter(owner=request.user)

    week_out = date.today() + timedelta(days=7)
    content['upcoming_tasks'] = user_tasks.filter(due_date__gt=date.today()).filter(due_date__lte=week_out).filter(completed=False).order_by('due_date')[:5]

    content['completed_tasks'] = user_tasks.filter(completed=True).order_by('due_date')[:5]

    content['overdue_tasks'] = user_tasks.filter(due_date__lte=date.today()).filter(completed=False).order_by('due_date')[:5]

    return render(request, 'website/task_menu.html', content)

@login_required
def task_detail(request, task_pk):
    content = {}
    user_tasks = TaskModel.objects.filter(owner=request.user)
    task = get_object_or_404(user_tasks, pk=task_pk)
    content['task'] = task
    task_completed = False
    if task.completed:
        task_completed = True
    content['task_completed'] = task_completed
    return render(request, 'website/task_detail.html', content)

@login_required
def manage_task_completed(request, task_pk):
    content = {}
    user_tasks = TaskModel.objects.filter(owner=request.user)
    task = get_object_or_404(user_tasks, pk=task_pk)
    if not task.completed:
        task.completed = True
        task.save()
    else:
        task.completed = False
        task.save()
    return redirect("task_detail", task_pk=task_pk)
