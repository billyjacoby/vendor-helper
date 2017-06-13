from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^profile/view/$', views.view_profile, name="view_profile"),
    url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),

]
