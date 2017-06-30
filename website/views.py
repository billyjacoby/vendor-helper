# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from reg_extras.forms import UserProfileRegistrationForm, EditUserProfileForm, EditUserForm
from website.forms import TaskModelForm, UserIncentiveModelForm
from django.contrib.auth.models import User

from datetime import date, timedelta, datetime

from website.models import IncentiveModel, TaskModel, UserIncentiveModel
# Create your views here.
def index(request):
    content = {}
    return render(request, 'website/index.html', content)

def about(request):
    content = {}
    return render(request, 'website/about.html', content)

def view_profile(request):
    profile = request.user.get_username()
    content = {
    "profile":profile,
    }
    return render(request, 'website/view_profile.html', content)

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

def user_dashboard(request):
    content = {}
    content['incentive_by_date'] = IncentiveModel.objects.filter(end_date__gte=date.today()).order_by('-date_added')[:5]

    username=request.user.id
    content['subscribed_incentives'] = IncentiveModel.objects.filter(end_date__gte=date.today()).filter(users_subscribed__id=username).order_by('end_date')

    five_days = date.today() + timedelta(days=7)
    content['five_days'] = five_days
    content['incentives_due_soon'] = IncentiveModel.objects.filter(end_date__gte=date.today()).filter(end_date__range=[date.today(), five_days]).order_by('end_date')
    incentive_long = False
    if content['incentives_due_soon'].count() > 4:
        content['incentives_due_soon'] = content['incentives_due_soon'][:4]
        incentive_long = True

    content['incentive_long'] = incentive_long

    content['users_tasks'] = TaskModel.objects.filter(owner=request.user).filter(due_date__gte=date.today()).filter(completed=False).filter(due_date__range=[date.today(), five_days]).order_by('due_date')
    tasks_long = False
    if content['users_tasks'].count() > 2:
        content['users_tasks'] = content['users_tasks'][:2]
        tasks_long = True
    content['tasks_long'] = tasks_long

    return render(request, 'website/user_dashboard.html', content)

def incentive_menu(request):
    month_choices = {
    "1" : "January",
    "2" : "February",
    "3" : "March",
    "4" : "April",
    "5" : "May",
    "6" : "June",
    "7" : "July",
    "8" : "August",
    "9" : "September",
    "10" : "October",
    "11" : "November",
    "12" : "December"
    }

    month = date.today().month
    if request.method == 'POST':
        month = request.POST['chosen-month']

    content = {}
    content['month_choices'] = month_choices
    content['month'] = month
    print "month: " + str(month)
    content['today'] = date.today()

    user = request.user.id
    one_week = date.today() + timedelta(days=7)
    subscribed_incentives = IncentiveModel.objects.filter(users_subscribed__id=user)
    subscribed_and_due = subscribed_incentives.filter(end_date__range=[date.today(), one_week]).order_by('end_date')
    content['subscribed_and_due'] = subscribed_and_due

    user_incentives = UserIncentiveModel.objects.filter(owner=user)
    completed_not_payed = user_incentives.filter(payed=False)
    content['completed_not_payed'] = completed_not_payed

    completed_payed = user_incentives.filter(payed=True)
    content['completed_payed'] = completed_payed


    subscribed_potential_payout = 0
    for item in subscribed_incentives:
        if item.payout:
            subscribed_potential_payout += item.payout
    content['subscribed_potential_payout'] = subscribed_potential_payout

    user_incentives_for_month = UserIncentiveModel.objects.filter(incentivemodel__end_date__month=month)

    """for item in user_incentives_for_month:
        print item
        print item.incentivemodel.end_date"""

    completed_user_incentives_for_month = user_incentives_for_month.filter(completed=True)
    payout_for_month = 0
    for item in completed_user_incentives_for_month:
        if item.payout:
            payout_for_month += item.payout
    content['payout_for_month'] = payout_for_month

    percent_complete = ((round(payout_for_month / subscribed_potential_payout, 3)) * 100)
    content['percent_complete'] = percent_complete

    return render(request, 'website/incentive_menu.html', content)

def incentive_detail(request, incentive_pk):
    incentive = get_object_or_404(IncentiveModel, pk=incentive_pk)
    content = {}
    content['incentive'] = incentive
    subscribed= False
    if request.user in incentive.users_subscribed.all():
        subscribed = True
    content['subscribed'] = subscribed

    user_incentives = UserIncentiveModel.objects.filter(owner=request.user).filter(incentivemodel__pk=incentive_pk)
    content['user_incentives'] = user_incentives

    return render(request, 'website/incentive_detail.html', content)

def manage_incentive_subscription(request, incentive_pk):
    incentive = get_object_or_404(IncentiveModel, pk=incentive_pk)
    content = {}
    if request.user in incentive.users_subscribed.all():
        incentive.users_subscribed.remove(request.user)
    else:
        incentive.users_subscribed.add(request.user)
    return redirect("incentive_detail", incentive_pk=incentive_pk)

def incentive_list(request):
    content = {}
    content['incentive_list'] = IncentiveModel.objects.filter(end_date__gte=date.today()).order_by('end_date')
    content['ended_incentive_list'] = IncentiveModel.objects.filter(end_date__lt=date.today()).order_by('end_date')
    return render(request, 'website/incentive_list.html', content)

def incentive_user_create(request, incentive_pk):
    content = {}
    incentive = IncentiveModel.objects.get(pk=incentive_pk)
    content['incentive'] = incentive
    if request.method=='POST':
        form = UserIncentiveModelForm(request.POST)
        content['form'] = form
        if form.is_valid():
            stock = form.save(commit=False)
            stock.incentivemodel = incentive
            stock.owner = request.user
            stock.save()
            return redirect('incentive_detail', incentive_pk=incentive_pk)
        else:
            content['form.errors'] = form.errors

    else:
        form = UserIncentiveModelForm()
        content['form'] = form
    return render(request, 'website/incentive_user_create.html', content)

def edit_user_incentive(request, incentive_pk, user_incentive_pk):
    content = {}
    content['incentive_pk'] = incentive_pk
    incentive = IncentiveModel.objects.get(pk=incentive_pk)
    content['incentive'] = incentive
    instance = UserIncentiveModel.objects.filter(owner=request.user).get(pk=user_incentive_pk)
    if request.method == 'POST':
        form = UserIncentiveModelForm(request.POST)
        content['form'] = form
        if form.is_valid():
            stock = form.save(commit=False)
            stock.incentivemodel = incentive
            stock.owner = request.user
            stock.pk = user_incentive_pk
            stock.save()
            return redirect('incentive_detail', incentive_pk=incentive_pk)
        else:
            content['form.errors'] = form.errors

    else:
        form = UserIncentiveModelForm(instance=instance)
        content['form'] = form
    return render(request, 'website/edit_user_incentive.html', content)

def incentive_user_delete(request, incentive_pk, user_incentive_pk):
    content = {}
    user_incentives = UserIncentiveModel.objects.filter(owner=request.user)
    user_incentive = get_object_or_404(user_incentives, pk=user_incentive_pk)
    user_incentive.delete()
    return redirect('incentive_detail', incentive_pk=incentive_pk)

def task_list(request, task_type="all"):
    content = {}
    task_list = []
    user_tasks = TaskModel.objects.filter(owner=request.user)
    if task_type == "upcoming":
        task_list = user_tasks.filter(due_date__gte=date.today()).order_by('due_date')
    elif task_type == "overdue":
        task_list = user_tasks.filter(completed=False).filter(due_date__lt=date.today()).order_by('due_date')
    elif task_type == "completed":
        task_list = user_tasks.filter(completed=True).order_by('due_date')
    else:
        task_list = user_tasks.order_by('due_date')
        task_type="all"

    content['task_list'] = task_list
    content['task_type'] = task_type
    return render(request, 'website/task_list.html', content)

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
            return redirect('task_menu')
        else:
            content['form.errors'] = form.errors
    else:
        form = TaskModelForm()
        content['form'] = form
    return render(request, 'website/create_task.html', content)

def edit_task(request, task_pk):
    content = {}
    content['task_pk']= task_pk
    instance = TaskModel.objects.filter(owner=request.user).get(pk=task_pk)
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        content['form'] = form
        if form.is_valid():
            stock = form.save(commit=False)
            stock.owner = request.user
            stock.pk = task_pk
            stock.save()
            return redirect('task_detail', task_pk=task_pk)
        else:
            content['form.errors'] = form.errors

    else:
        form = TaskModelForm(instance=instance)
        content['form'] = form
    return render(request, 'website/edit_task.html', content)

def delete_task(request, task_pk):
    content = {}
    user_tasks = TaskModel.objects.filter(owner=request.user)
    user_task = get_object_or_404(user_tasks, pk=task_pk)
    user_task.delete()
    return redirect('task_menu')

def task_menu(request):
    content = {}

    user_tasks = TaskModel.objects.filter(owner=request.user)

    week_out = date.today() + timedelta(days=7)
    content['upcoming_tasks'] = user_tasks.filter(due_date__gte=date.today()).filter(due_date__lte=week_out).filter(completed=False).order_by('due_date')[:5]

    content['completed_tasks'] = user_tasks.filter(completed=True).order_by('due_date')[:5]

    content['overdue_tasks'] = user_tasks.filter(due_date__lte=date.today()).filter(completed=False).order_by('due_date')[:5]

    return render(request, 'website/task_menu.html', content)

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
