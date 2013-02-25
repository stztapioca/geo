from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^italy/$', 'italy.views.index'),
    url(r'^italy/(?P<regione_id>\d+)/$', 'italy.views.detail_regione') ,
    url(r'^italy/(?P<regione_name>\w+)/$', 'italy.views.detail_regione') ,
    url(r'^admin/', include(admin.site.urls)),
)
