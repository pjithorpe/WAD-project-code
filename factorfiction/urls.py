from django.conf.urls import url
from factorfiction import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fofgame/$', views.fofgame, name='fofgame'),
	url(r'^submit_page/$', views.submit_page, name='submit_page'),
]
