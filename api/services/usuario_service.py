from ..models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


def registrar_usuario(data):
    """
    Crea un nuevo usuario con datos encriptados y contraseña hasheada,
    validando que el correo no exista previamente.
    """
    if Usuario.objects.filter(email=data['email']).exists():
        raise ValidationError("El correo ya está registrado.")

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


def autenticar_usuario(email, contraseña):
    if not email or not contraseña:
        return None, "Faltan datos"

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None, "Usuario no encontrado"

    if not check_password(contraseña, usuario.contraseña):
        return None, "Contraseña incorrecta"

    # Si pasa validación, se genera el token
    refresh = RefreshToken.for_user(usuario)

    respuesta = {
        "token": str(refresh.access_token),
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "rol": usuario.rol,
        "id": usuario.id
    }

    return respuesta, None