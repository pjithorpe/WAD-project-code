from django.conf.urls import url, include
from django.contrib import admin
from factorfiction import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^factorfiction/', include('factorfiction.urls')),
	url(r'^fofgame/', views.fofgame, name='fofgame'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
