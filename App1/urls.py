from django.urls import path
from App1.views import *

urlpatterns = [
    path('inicio', inicio, name = "inicio"),
    path('formu1', form1, name = "form1"),
    path('formu2', form2, name = "form2"),
    path('formu3', form3, name = "form3"),
    path('busqueda', busquedaPronostico, name = "buscarpronos"),
    path('respuesta', respuestaPronostico, name = "respuestapronos"),
]