# api/services/encuesta_service.py
from api.models import Visitante

def validar_cedula(cedula):
    """Verifica si el visitante con esa cédula está registrado."""
    return Visitante.objects.filter(cedula_pasaporte=cedula).exists()
