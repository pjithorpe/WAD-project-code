from django.conf.urls import url
from factorfiction import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fofgame/$', views.fofgame, name='fofgame'),
	url(r'^submit_page/$', views.submit_page, name='submit_page'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	
]
