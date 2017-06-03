from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog_home, name="blog home"),
    url(r'^view/(?P<slug>[^\.]+)/', views.view_post, name='view_post'),
    url(r'^category/(?P<slug>[^\.]+)/', views.view_category, name="view_category"),
]
