from django.conf.urls.defaults import patterns, include, url
from rec import views
import settings
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
   url(r'^$', views.startPage),
   url(r'^(?P<uId>\d+)/$', views.logoutPage),
   url(r'^signup/$', views.signup),
   url(r'^(?P<sId>\d+)/initial/$',views.initialPage),
   url(r'^(?P<sId>\d+)/home/$',views.homePage),
   url(r'^(?P<sId>\d+)/profile/$',views.profilePage),
   url(r'^(?P<sId>\d+)/profile/pswdchange/$',views.changePassword),
   url(r'^(?P<sId>\d+)/movie/(?P<mId>\d+)/$',views.movie),
   url(r'^(?P<sId>\d+)/book/(?P<bId>\d+)/$',views.book),
   url(r'^(?P<sId>\d+)/recommendM/$', views.movieRec),
   url(r'^(?P<sId>\d+)/recommendB/$', views.bookRec),
   url(r'^(?P<sId>\d+)/friend/(?P<pId>\d+)/$',views.friends),
   url(r'^admin/', include(admin.site.urls)),
   #url(r'^(?P<uId>\d+)/$', views.initial),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
