from django.conf.urls import url

from . import views

app_name = 'projects'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?i)(?P<project_slug>[\w]+)\/?$', views.detail, name='detail'),
]
