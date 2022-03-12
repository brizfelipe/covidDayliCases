from django.urls import path
from . import views
urlpatterns = [
    path('mongoDB', views.refreshMongoDB, name='refreshMongoDB'),
    path('postgres', views.refreshPostgres, name='refreshPostgres'),
]