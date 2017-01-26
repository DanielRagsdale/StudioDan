from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^linkedin$', views.linkedin, name='linkedin')
]
