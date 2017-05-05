from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<room_x>[0-9]+)/(?P<room_y>[0-9]+)/(?P<direction>[NESW])$', views.room, name='room'),
]
