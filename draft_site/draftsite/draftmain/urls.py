from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'draftmain'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<player_id>[0-9]+)/$', views.playerView, name="playerView"),
]