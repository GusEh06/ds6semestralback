# api/services/encuesta_service.py
from api.models import Visitante, RegistroVisita, Encuesta
from django.core.exceptions import ObjectDoesNotExist

def validar_cedula(cedula):
    """Verifica si el visitante con esa cédula está registrado."""
    return Visitante.objects.filter(cedula_pasaporte=cedula).exists()

def guardar_encuesta(visita_id, formulario):
    """Guarda una encuesta asociada a una visita."""
    try:
        visita = RegistroVisita.objects.get(id=visita_id)
        encuesta = Encuesta.objects.create(
            visita=visita,
            formulario=formulario
        )
        return encuesta, None
    except RegistroVisita.DoesNotExist:
        return None, 'Registro de visita no encontrado'
    except Exception as e:
        return None, str(e)
