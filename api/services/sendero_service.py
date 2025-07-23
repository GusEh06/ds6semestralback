from ..models import Sendero
from django.shortcuts import get_object_or_404


def obtener_sendero(id_sendero):
    """
    Devuelve un sendero por su ID.
    """
    return get_object_or_404(Sendero, pk=id_sendero)


def listar_todos_los_senderos():
    """
    Devuelve todos los senderos registrados.
    """
    return Sendero.objects.all()
