from rest_framework import viewsets
from .models import Visitante, Encuesta
from .serializers import VisitanteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    UsuarioSerializer, SenderoSerializer, SenderoFotoSerializer
)
from .services import usuario_service, sendero_service, foto_sendero_service
from .services import encuesta_service
from .models import Encuesta, Visitante, RegistroVisita



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


@api_view(['POST'])
def validar_cedula_visitante(request):
    cedula = request.data.get('cedula')
    if not cedula:
        return Response({'error': 'Cédula no proporcionada'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        visitante = Visitante.objects.get(cedula=cedula)
        return Response({'mensaje': 'Visitante registrado', 'visitante_id': visitante.id}, status=status.HTTP_200_OK)
    except Visitante.DoesNotExist:
        return Response({'error': 'Visitante no registrado'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def guardar_encuesta(request):
    visita_id = request.data.get('visita_id')  
    formulario = request.data.get('formulario')

    if not visita_id or not formulario:
        return Response({'error': 'Datos incompletos'}, status=status.HTTP_400_BAD_REQUEST)

    encuesta, error = encuesta_service.guardar_encuesta(visita_id, formulario)

    if error:
        if error == 'Registro de visita no encontrado':
            return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'mensaje': 'Encuesta guardada correctamente', 'encuesta_id': encuesta.id}, status=status.HTTP_201_CREATED)


