from rest_framework import viewsets
from .models import Visitante
from .serializers import VisitanteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (UsuarioSerializer, SenderoSerializer, SenderoFotoSerializer)
from .services import usuario_service, sendero_service, foto_sendero_service
from .serializers import VisitanteSerializer
from .models import Visitante, RegistroVisita, Sendero

    
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
# RELEZ
# ==============================

@api_view(['GET'])
def obtener_visitante_por_cedula(request, cedula):
    visitante = Visitante.objects.filter(cedula_pasaporte=cedula).first()
    if visitante:
        serializer = VisitanteSerializer(visitante)
        return Response(serializer.data)
    return Response({"detail": "Visitante no encontrado."}, status=404)


@api_view(['POST'])
def registrar_visita(request):
    cedula = request.data.get("cedula_pasaporte")
    sendero_nombre = request.data.get("sendero_visitado")
    razon = request.data.get("razon_visita")

    if not cedula or not sendero_nombre or not razon:
        return Response({"detail": "Faltan datos requeridos."}, status=400)

    visitante = Visitante.objects.filter(cedula_pasaporte=cedula).first()
    if not visitante:
        return Response({"detail": "Visitante no encontrado."}, status=404)

    # ✅ Verificar que el sendero exista
    sendero = Sendero.objects.filter(nombre_sendero=sendero_nombre).first()
    if not sendero:
        return Response({"detail": "El sendero no existe."}, status=400)

    # Ahora sí guardar
    visita = RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=razon
    )

    return Response({"mensaje": "Visita registrada correctamente."}, status=201)



@api_view(['POST'])
def registrar_visitante_y_visita(request):
    data = request.data

    campos_obligatorios = [
        "cedula_pasaporte", "nombre_visitante", "nacionalidad", "adulto_nino",
        "telefono", "genero", "sendero_visitado", "razon_visita"
    ]

    # Validar campos vacíos
    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            return Response({"detail": f"Campo '{campo}' es requerido."}, status=400)

    # Verificar que el sendero exista
    sendero_nombre = data["sendero_visitado"]
    sendero = Sendero.objects.filter(nombre_sendero=sendero_nombre).first()
    if not sendero:
        return Response({"detail": "El sendero no existe."}, status=400)

    # Validar si ya existe el visitante
    if Visitante.objects.filter(cedula_pasaporte=data["cedula_pasaporte"]).exists():
        return Response({"detail": "El visitante ya está registrado."}, status=400)

    # Crear visitante
    visitante = Visitante.objects.create(
        cedula_pasaporte=data["cedula_pasaporte"],
        nombre_visitante=data["nombre_visitante"],
        nacionalidad=data["nacionalidad"],
        adulto_nino=data["adulto_nino"],
        telefono=data["telefono"],
        genero=data["genero"]
    )

    # Crear visita asociada
    RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=data["razon_visita"]
    )

    return Response({"mensaje": "Visitante y visita registrados correctamente."}, status=201)

@api_view(['POST'])
def registrar_visita_por_id(request):
    visitante_id = request.data.get("visitante_id")
    sendero_nombre = request.data.get("sendero_visitado")
    razon = request.data.get("razon_visita")

    if not visitante_id or not sendero_nombre or not razon:
        return Response({"detail": "Faltan datos requeridos."}, status=400)

    try:
        visitante = Visitante.objects.get(id=visitante_id)
    except Visitante.DoesNotExist:
        return Response({"detail": "Visitante no encontrado."}, status=404)

    sendero = Sendero.objects.filter(nombre_sendero=sendero_nombre).first()
    if not sendero:
        return Response({"detail": "El sendero no existe."}, status=400)

    RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=razon
    )

    return Response({"mensaje": "Visita registrada correctamente."}, status=201)



