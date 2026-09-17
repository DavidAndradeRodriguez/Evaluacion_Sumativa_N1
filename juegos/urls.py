from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio.html'),
    path('juegos/', views.lista_juegos, name='lista_juegos'),
    path('juegos/<int:id>/', views.detalle_juego, name='detalle_juego'),
]