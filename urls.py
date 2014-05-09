from django.conf.urls.defaults import patterns, include, url
from rec import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
   url(r'^$', views.start),
   url(r'^signup/$', views.signup),
   url(r'^(?P<uId>\d+)/$', views.initial),
   url(r'^(?P<uId>\d+)/home/$',views.home),
   url(r'^(?P<uId>\d+)/book/(?P<bId>\d+)/$',views.book),
   url(r'^(?P<uId>\d+)/movie/(?P<mId>\d+)/$',views.movie),
   url(r'^profile/(?P<userId>\d+)/$',views.profile),
   url(r'^changepassword/(?P<usersId>\d+)/$',views.changepassword),
   url(r'^confirm/(?P<usersId>\d+)/$',views.confirm),
   url(r'^(?P<uId>\d+)/movie/Recommend/$', views.movieRec),
   
   url(r'^admin/', include(admin.site.urls)),
)

