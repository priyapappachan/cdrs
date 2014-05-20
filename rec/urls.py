from django.conf.urls.defaults import patterns,  url, include
from django.contrib import admin
admin.autodiscover()
from rec import views

urlpatterns = patterns('',
	 url(r'^admin/', include(admin.site.urls)),
	 url(r'^$', views.start),
	 url(r'^(?P<name>\d+)/$',views.home)
	 url(r'^(?P<name>\d+)/movie/$',views.movie)
)
