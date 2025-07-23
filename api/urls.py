from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VisitanteViewSet, registro_usuario, obtener_usuario, mostrar_sendero, listar_senderos, mostrar_foto_sendero, listar_fotos_senderos
)

router = DefaultRouter()
router.register(r'visitantes', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Usuarios
    path('registro/', registro_usuario, name='registro-usuario'),
    path('usuario/<int:id>/', obtener_usuario, name='obtener-usuario'),

    # Senderos
    path('sendero/<int:id>/', mostrar_sendero, name='mostrar-sendero'),
    path('senderos/', listar_senderos, name='listar-senderos'),

    # Fotos de senderos
    path('foto-sendero/<int:id>/', mostrar_foto_sendero, name='mostrar-foto-sendero'),
    path('fotos-senderos/', listar_fotos_senderos, name='listar-fotos-senderos'),
]