from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from project.views import add_project,add_project2

# Uncomment the next two lines to enable the admin:
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import patterns,url
from project.views import ProjectListing, ProjectCreate, ProjectDetail, ProjectUpdate,ProjectDelete
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
   # (r'^home/$',TemplateView.as_view(template_name='home.html')),
    url(r'^add-project/$',add_project2,name="add-project"),
    url(r'^list-project/$',login_required(ProjectListing.as_view()),name='listing'),
    url(r'^create-project/$',ProjectCreate.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',ProjectDetail.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/update/$', ProjectUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ProjectDelete.as_view(), name='delete'),
    # Examples:
    # url(r'^$', 'drnau_project.views.home', name='home'),
    # url(r'^drnau_project/', include('drnau_project.foo.urls')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^project/', include('project.urls', namespace='project')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
