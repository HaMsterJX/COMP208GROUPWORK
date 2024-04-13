# team/urls.py

from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'player/', include(('player.urls', 'player'))),
    path('', views.home, name='home'),
    path('login.html/', views.login_view, name='login'),
]
