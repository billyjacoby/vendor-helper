"""wireframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

# for regsitration
from reg_extras.forms import UserProfileRegistrationForm
from registration.views import RegistrationView
from reg_extras import regbackend
from django.views.generic import RedirectView

from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/password/$', RedirectView.as_view(url="/accounts/password/change/")),
    url(r'^', include('website.urls')),
    url(r'^blog/', include('blog.urls')),
    #for account registration
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view() ,name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True))
]

"""
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
"""
