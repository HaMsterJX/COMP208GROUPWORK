# player/urls.py

from django.urls import path
from . import views
from .views import media_list

urlpatterns = [
    path(r'', views.index, name='player'),
    path('media_list', media_list, name='media_list'),
    path(r'load_music', views.load_music, name='load_music'),
]
