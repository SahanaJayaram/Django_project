from django.conf.urls import patterns, include, url
from django.contrib import admin
#from stars import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$','stars.views.home',name='home'),
     url(r'^registration','stars.views.registration',name='registration'),
     url(r'^login','stars.views.login',name='login'),
	url(r'^Person_list','stars.views.Person_list',name='Person_list'),
   url(r'^Login_list','stars.views.Login_list',name='Login_list'),
   
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
