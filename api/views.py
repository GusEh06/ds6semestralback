from rest_framework import viewsets
from .models import Visitante
from .serializers import VisitanteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    UsuarioSerializer, SenderoSerializer, SenderoFotoSerializer
)
from .services import usuario_service, sendero_service, foto_sendero_service
from .services import dashboard_service  # Importar el nuevo servicio


    
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


# ==============================
# Dashboard Endpoints
# ==============================

@api_view(['GET'])
def visitas_recientes(request):
    """
    Obtiene las visitas recientes con toda la información necesaria.
    Retorna: Fecha, Nombre, Adulto, Niño, Nacionalidad, Motivo de Visita, Sendero, Hora de Entrada, Teléfono
    """
    try:
        visitas = dashboard_service.obtener_visitas_recientes()
        return Response(visitas, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Error al obtener visitas recientes", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def visitantes_hoy(request):
    """
    Retorna el conteo de visitantes de hoy.
    """
    try:
        count = dashboard_service.contar_visitantes_hoy()
        return Response({"visitantes_hoy": count}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Error al contar visitantes de hoy", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def encuestas_hoy(request):
    """
    Retorna el conteo de encuestas llenadas hoy.
    """
    try:
        count = dashboard_service.contar_encuestas_hoy()
        return Response({"encuestas_hoy": count}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Error al contar encuestas de hoy", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def visitantes_por_pais(request):
    """
    Retorna el conteo de visitantes agrupados por país/nacionalidad.
    """
    try:
        datos = dashboard_service.obtener_visitantes_por_pais()
        return Response(datos, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Error al obtener visitantes por país", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def visitantes_por_sendero(request):
    """
    Retorna el conteo de visitantes agrupados por sendero.
    """
    try:
        datos = dashboard_service.obtener_visitantes_por_sendero()
        return Response(datos, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": "Error al obtener visitantes por sendero", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )