from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VisitanteViewSet, registro_usuario, obtener_usuario, mostrar_sendero, listar_senderos, mostrar_foto_sendero, listar_fotos_senderos
,login_usuario
)
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'visitantes', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Usuarios
    path('registro/', registro_usuario, name='registro-usuario'),
    path('usuario/<int:id>/', obtener_usuario, name='obtener-usuario'),
    path('login/', login_usuario, name='login-usuario'),

    # Senderos
    path('sendero/<int:id>/', mostrar_sendero, name='mostrar-sendero'),
    path('senderos/', listar_senderos, name='listar-senderos'),

    # Fotos de senderos
    path('foto-sendero/<int:id>/', mostrar_foto_sendero, name='mostrar-foto-sendero'),
    path('fotos-senderos/', listar_fotos_senderos, name='listar-fotos-senderos'),

    #Visitantes
    path('registrar_visitante_y_visita/', views.registrar_visitante_y_visita, name='registrar_visitante_y_visita'),
    path('registrar_visita_existente/', views.registrar_visita_existente, name='registrar_visita_existente'),
    path('visitante_por_cedula/', views.obtener_nombre_visitante, name='visitante_por_cedula'),
    path('senderos/', views.listar_senderos, name='listar_senderos'),
]