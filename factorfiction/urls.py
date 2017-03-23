from django.conf.urls import url
from factorfiction import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fofgame/$', views.fofgame, name='fofgame'),
	url(r'^submit_page/$', views.submit_page, name='submit_page'),
	url(r'^page/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
	url(r'^register/$', views.register, name='register'),
	url(r'^update_profile/$', views.update_profile, name='update_profile'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^about/$', views.about, name='about'),
	url(r'^search/$', views.search, name='search'),
	url(r'^my_profile/$', views.my_profile, name='my_profile'),
	url(r'^vote_fact/$', views.vote_fact, name='vote_fact'),
	url(r'^vote_fiction/$', views.vote_fiction, name='vote_fiction'),
	url(r'^page/(?P<page_name_slug>[\w\-]+)/$',
		views.show_page, name='show_page'),
	url(r'^user/(?P<username>[\w\-]+)/$',
		views.show_user_page, name='show_user_page'),

]
