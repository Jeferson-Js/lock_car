from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('suporte/', views.suporte, name="suporte"),
    path('novidades/', views.novidades, name="novidades"),
    path('reservas/', views.reservas, name="reservas"),
    path('promocoes/', views.promocoes, name="promocoes"),
]


