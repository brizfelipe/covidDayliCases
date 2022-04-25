from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.register, name='createLogin'),
    path('',views.subscription,name='subscription'),
    path('singin',views.singIn,name='singin'),
    path('menu',views.menu,name='menu')
]