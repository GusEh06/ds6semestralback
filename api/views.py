from rest_framework import viewsets
from .models import Visitante, Usuario
from .serializers import VisitanteSerializer, ComentarioSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UsuarioSerializer, SenderoSerializer, SenderoFotoSerializer
)
from .services import usuario_service, sendero_service, foto_sendero_service, comentario_service, valoracion_service


    
class VisitanteViewSet(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer

# ==============================
# Samir
# ==============================
@api_view(['POST'])
def registro_usuario(request):
    """Crea un usuario nuevo."""
    usuario = usuario_service.registrar_usuario(request.data)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def obtener_usuario(request, id):
    """Obtiene un usuario por ID."""
    usuario = usuario_service.obtener_usuario(id)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


@api_view(['GET'])
def mostrar_sendero(request, id):
    """Devuelve la información de un sendero."""
    sendero = sendero_service.obtener_sendero(id)
    serializer = SenderoSerializer(sendero)
    return Response(serializer.data)


@api_view(['GET'])
def listar_senderos(request):
    """Devuelve todos los senderos."""
    senderos = sendero_service.listar_todos_los_senderos()
    serializer = SenderoSerializer(senderos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mostrar_foto_sendero(request, id):
    """Devuelve la foto de un sendero específico."""
    foto = foto_sendero_service.obtener_foto_sendero(id)
    serializer = SenderoFotoSerializer(foto)
    return Response(serializer.data)


@api_view(['GET'])
def listar_fotos_senderos(request):
    """Devuelve todas las fotos de senderos."""
    fotos = foto_sendero_service.obtener_todas_fotos_sendero()
    serializer = SenderoFotoSerializer(fotos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_usuario(request):
    email = request.data.get("email")
    contraseña = request.data.get("contraseña")

    datos, error = usuario_service.autenticar_usuario(email, contraseña)

    if error:
        return Response({"detail": error}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(datos, status=status.HTTP_200_OK)




#endpoints de comentarios(Javier)
@api_view(['POST'])
def agregar_comentario(request):
    data = request.data.copy()
    serializer = ComentarioSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    comentario = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comentarios_por_sendero(request, sendero_id):
    """ Devuelve todos los comentarios asociados a un sendero específico"""
    comentarios = comentario_service.listar_comentarios_por_sendero(sendero_id)
    serializer = ComentarioSerializer(comentarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def valoracion_promedio(request, sendero_id):
    """Calcula y devuelve la valoración promedio de los comentarios de un sendero específico."""
    promedio = valoracion_service.obtener_valoracion_promedio(sendero_id)
    return Response({
        "sendero_id": sendero_id,
        "valoracion_promedio": promedio
    })

@api_view(['GET'])
def valoraciones_por_sendero(request, sendero_id):
    data = valoracion_service.obtener_valoraciones_por_sendero(sendero_id)
    return Response(data)

