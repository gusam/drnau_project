__author__ = 'Franco'
from django.conf.urls import patterns, include, url
from project.views import  MainView,Prueba
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^crear/$',MainView.as_view(),name='create'),
                       url(r'^prueba/$',login_required(Prueba.as_view()),name='prueba')

)
