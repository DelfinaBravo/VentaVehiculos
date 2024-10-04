from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    #-->URL, FUNCION, NOMBRE PARA HTML
    path('',Home,name='inicio'),
    path('vehiculo/<int:Codigo>/', detalle_vehiculo, name='detalle_vehiculo'),
    path('agregar/',Agregar,name='agregar'),
    path('visualizar/',ver_Vehiculos,name='visualizar'),
    path('modificar/<Codigo>/',Modificar_Vehiculos,name='modificar'),
    path('eliminar/<Codigo>/',Eliminar_Vehiculos,name='eliminar'),
    path('logouts/',salir,name='logouts'),
]
