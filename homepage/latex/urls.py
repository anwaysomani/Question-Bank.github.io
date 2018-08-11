from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^question/', views.question, name='question'),
        url(r'^$', views.index, name='index'),
        url(r'form/$', views.form, name='form'),
        url(r'list/$', views.list, name='list'),
]