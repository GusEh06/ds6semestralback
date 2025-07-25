from api.models import Visitante, RegistroVisita, Sendero
from api.serializers import VisitanteSerializer
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError


def obtener_visitante_por_cedula(cedula):
    visitante = Visitante.objects.filter(cedula_pasaporte=cedula).first()
    if not visitante:
        raise ValidationError({"detail": "Visitante no encontrado."})
    return visitante


def registrar_visita(cedula, sendero_nombre, razon):
    if not cedula or not sendero_nombre or not razon:
        raise ValidationError({"detail": "Faltan datos requeridos."})

    visitante = Visitante.objects.filter(cedula_pasaporte=cedula).first()
    if not visitante:
        raise ValidationError({"detail": "Visitante no encontrado."})

    sendero = Sendero.objects.filter(nombre_sendero=sendero_nombre).first()
    if not sendero:
        raise ValidationError({"detail": "El sendero no existe."})

    RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=razon,
        fecha_visita=now()
    )

    return {"mensaje": "Visita registrada correctamente."}


def registrar_visitante_y_visita(data):
    campos_obligatorios = [
        "cedula_pasaporte", "nombre_visitante", "nacionalidad", "adulto_nino",
        "telefono", "genero", "sendero_visitado", "razon_visita"
    ]

    for campo in campos_obligatorios:
        if campo not in data or not data[campo]:
            raise ValidationError({"detail": f"Campo '{campo}' es requerido."})

    if Visitante.objects.filter(cedula_pasaporte=data["cedula_pasaporte"]).exists():
        raise ValidationError({"detail": "El visitante ya está registrado."})

    sendero = Sendero.objects.filter(nombre_sendero=data["sendero_visitado"]).first()
    if not sendero:
        raise ValidationError({"detail": "El sendero no existe."})

    visitante = Visitante.objects.create(
        cedula_pasaporte=data["cedula_pasaporte"],
        nombre_visitante=data["nombre_visitante"],
        nacionalidad=data["nacionalidad"],
        adulto_nino=data["adulto_nino"],
        telefono=data["telefono"],
        genero=data["genero"]
    )

    RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=data["razon_visita"],
        fecha_visita=now()
    )

    return {"mensaje": "Visitante y visita registrados correctamente."}


def registrar_visita_por_id(visitante_id, sendero_nombre, razon):
    if not visitante_id or not sendero_nombre or not razon:
        raise ValidationError({"detail": "Faltan datos requeridos."})

    visitante = Visitante.objects.filter(id=visitante_id).first()
    if not visitante:
        raise ValidationError({"detail": "Visitante no encontrado."})

    sendero = Sendero.objects.filter(nombre_sendero=sendero_nombre).first()
    if not sendero:
        raise ValidationError({"detail": "El sendero no existe."})

    RegistroVisita.objects.create(
        visitante=visitante,
        sendero_visitado=sendero.nombre_sendero,
        razon_visita=razon,
        fecha_visita=now()
    )

    return {"mensaje": "Visita registrada correctamente."}
