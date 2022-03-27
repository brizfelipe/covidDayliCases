from django.urls import path,include
from . import views
from .views import CovidViewSet,CovidCasesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('consultas', CovidViewSet, basename='consultas')
router.register('covidCases',CovidCasesViewSet, basename='covidCases')


urlpatterns = [
    path('consulta/', views.consultaApiCovid, name='consultaApiCovid'),
    path('login/', views.createLogin, name='createLogin'),
    path('',include(router.urls))
]