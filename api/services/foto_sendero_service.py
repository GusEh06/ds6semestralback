from ..models import SenderoFoto
from django.shortcuts import get_object_or_404


def obtener_foto_sendero(id_sendero):
    """
    Devuelve la foto asociada a un sendero.
    """
    return get_object_or_404(SenderoFoto, pk=id_sendero)


def obtener_todas_fotos_sendero():
    """
    Devuelve todas las fotos de senderos (si fueran varias por sendero).
    """
    return SenderoFoto.objects.all()
    