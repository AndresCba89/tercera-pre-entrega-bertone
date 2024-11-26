from django.urls import path
from AppAsb import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    #path('usuario/', views.usuario, name='usuario'),
    #path('paciente/', views.paciente, name='paciente'),
    #path('derivante/', views.derivante, name='derivante'),
    #path('analisis/', views.analisis, name='analisis'),
    path('us_form/', views.ususario_form, name='us_form'),
    path('pte_form/', views.paciente_form, name='pte_form'),
    path('dev_form/', views.derivante_form, name='dev_form'),
    path('an_form/', views.analisis_form, name='an_form'),
    #path('inicio/', views.busquedausuario, name='inicio'),
    path('buscar/', views.buscar, name='search'),
]
