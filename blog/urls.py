from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.BlogHome.as_view(), name="blog home"),
    url(r'^news/$', views.SiteNewsPage.as_view(), name="site_news_page"),
    url(r'^view/(?P<slug>[-\w]+)/', views.ArticleDetail.as_view(), name='view_post'),
    url(r'^category/$', views.CategoryHome.as_view(), name='category'),
    url(r'^category/(?P<slug>[-\w]+)/', views.CategorySingle.as_view(), name="view_category"),

]
