from django.conf.urls import url
from . import views          
	

urlpatterns = [
		url(r'^create_users$', views.create),
		url(r'^users$', views.users),
		url(r'^submit$', views.users),
		url(r'^', views.index),
		
		
]

