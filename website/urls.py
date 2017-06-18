from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^profile/view/$', views.view_profile, name="view_profile"),
    url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
    url(r'^incentive/(?P<incentive_pk>[0-9]+)/$', views.incentive_detail, name="incentive_detail"),
    url(r'^dashboard/$', views.user_dashboard, name="user_dashboard"),
    url(r'^incentive/subscribe/(?P<incentive_pk>[0-9]+)/$', views.manage_incentive_subscription, name="manage_incentive_subscription"),
    url(r'^incentive/list/$', views.incentive_list, name="incentive_list"),
    url(r'^tasks/create/$', views.create_task, name="create_task"),
    url(r'^tasks/menu/$', views.task_menu, name="task_menu"),
    url(r'^tasks/(?P<task_pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^tasks/completed/(?P<task_pk>[0-9]+)/$', views.manage_task_completed, name='manage_task_completed'),

]
