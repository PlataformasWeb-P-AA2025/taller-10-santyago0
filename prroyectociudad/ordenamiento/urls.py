"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('listar/parroquia/', views.listar_parroquia,
            name='listar_parroquias'),
        path('crear/parroquia/', views.crear_parroquia,
            name='crear_parroquia'),
        path('listar_barrio', views.listar_barrio,
            name='listar_barrios'),
        path('crear/barrio/', views.crear_barrio,
            name='crear_barrio')
 ]
