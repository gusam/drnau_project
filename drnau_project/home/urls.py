__author__ = 'Franco'
from django.conf.urls import patterns, include, url
from project.views import MainView
from home.views import Login,Logout

urlpatterns = patterns('',
                        # url(r'^login2$', 'django.contrib.auth.views.login', {'template_name': 'home/index.html'},
                        #     name='login'),
                       url(r'^cerrar$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^crear/$',MainView.as_view(),name='create'),
                       url(r'^login/$',Login.as_view(),name='login'),
                       url(r'^logout/$',Logout.as_view(),name='cerrar'),

)
