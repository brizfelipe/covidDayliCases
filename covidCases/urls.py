from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'),name='home'),
    path('api/',include('api.urls'),name='api'),
    path('user/',include('user.urls'),name='user'),
]
