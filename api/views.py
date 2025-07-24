from rest_framework import viewsets
from .models import RegistroVisita, Sendero, Visitante
from .serializers import RegistroVisitaSerializer, VisitanteSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UsuarioSerializer, SenderoSerializer, SenderoFotoSerializer
from .services import usuario_service, sendero_service, foto_sendero_service


    
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

@api_view(['POST'])
def registrar_visitante_y_visita(request):
    #Recibe los datos personales del visitante y los datos de la visita en un solo JSON.
    #Crea primero al visitante y luego el registro de la visita asociado.

    visitante_data = request.data.get('visitante')
    visita_data = request.data.get('visita')

    visitante_serializer = VisitanteSerializer(data=visitante_data)
    if visitante_serializer.is_valid():
        visitante = visitante_serializer.save()
        visita_data['visitante'] = visitante.id
        visita_serializer = RegistroVisitaSerializer(data=visita_data)
        if visita_serializer.is_valid():
            visita_serializer.save()
            return Response({'mensaje': 'Visitante y visita registrada'}, status=201)
        return Response(visita_serializer.errors, status=400)
    return Response(visitante_serializer.errors, status=400)


@api_view(['POST'])
def registrar_visita_existente(request):
    #Busca un visitante por cédula y registra una nueva visita para él.

    cedula = request.data.get('cedula')
    motivo = request.data.get('motivo')
    sendero_id = request.data.get('sendero')
    try:
        visitante = Visitante.objects.get(cedula=cedula)
        visita = RegistroVisita.objects.create(visitante=visitante, motivo=motivo, sendero_id=sendero_id)
        return Response({'mensaje': 'Visita registrada con éxito'}, status=201)
    except Visitante.DoesNotExist:
        return Response({'error': 'Visitante no encontrado'}, status=404)


@api_view(['GET'])
def obtener_nombre_visitante(request):
    #Recibe una cédula por parámetro GET y retorna el nombre del visitante si existe.
    
    cedula = request.GET.get('cedula')
    try:
        visitante = Visitante.objects.get(cedula=cedula)
        return Response({'nombre': visitante.nombre})
    except Visitante.DoesNotExist:
        return Response({'error': 'Visitante no encontrado'}, status=404)
    


    
@api_view(['GET'])
def listar_senderos(request):
    #Devuelve una lista con todos los senderos disponibles (id y nombre).

    senderos = Sendero.objects.all()
    data = [{'id': s.id, 'nombre': s.nombre} for s in senderos]
    return Response(data)

