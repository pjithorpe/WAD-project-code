from django.conf.urls import url
from factorfiction import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fofgame$', views.fofgame, name='fofgame'),
]
