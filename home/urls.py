from django.urls import path
from . import views
urlpatterns = [
    path('postgres', views.refreshPostgres, name='refreshPostgres'),
]
