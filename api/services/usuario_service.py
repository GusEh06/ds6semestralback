from ..models import Usuario
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404


def registrar_usuario(data):
    """
    Crea un nuevo usuario con datos encriptados y contraseña hasheada.
    """
    usuario = Usuario(
        email=data['email'],
        nombre=data['nombre'],
        apellido=data['apellido'],
        contraseña=make_password(data['contraseña']),
        rol=data.get('rol', Usuario.Rol.USER)
    )
    usuario.save()
    return usuario


def obtener_usuario(id_usuario):
    """
    Devuelve un usuario por su ID.
    """
    return get_object_or_404(Usuario, pk=id_usuario)
