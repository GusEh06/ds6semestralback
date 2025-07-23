from django.db import models
from cryptography.fernet import Fernet
from decouple import config
from django.contrib.auth.hashers import make_password, check_password


# ==============================
# Clave de encriptación desde .env
# ==============================
CLAVE_ENCRIPTACION = config('CLAVE_ENCRIPTACION')
fernet = Fernet(CLAVE_ENCRIPTACION)


# ==============================
# Funciones para cifrar y descifrar
# ==============================
def encriptar(valor):
    """Encripta un valor antes de guardarlo en la BD."""
    if valor is None:
        return None
    return fernet.encrypt(valor.encode()).decode()


def desencriptar(valor):
    """Desencripta un valor al leerlo de la BD."""
    if valor is None:
        return None
    return fernet.decrypt(valor.encode()).decode()


# ==============================
# Campo personalizado encriptado
# ==============================
class CampoEncriptado(models.TextField):
    """Campo de texto que se encripta automáticamente en la BD."""

    def get_prep_value(self, value):
        if value:
            return encriptar(value)
        return value

    def from_db_value(self, value, expression, connection):
        if value:
            return desencriptar(value)
        return value


# ==============================
# MODELOS
# ==============================

class Visitante(models.Model):
    cedula_pasaporte = CampoEncriptado(max_length=255)
    nombre_visitante = CampoEncriptado(max_length=255)
    nacionalidad = CampoEncriptado(max_length=255)
    adulto_nino = models.CharField(max_length=255)
    telefono = CampoEncriptado(max_length=255)
    genero = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_visitante}"


class Sendero(models.Model):
    nombre_sendero = models.CharField(max_length=50)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_sendero


class SenderoFoto(models.Model):
    id_sendero = models.OneToOneField(Sendero, on_delete=models.CASCADE, primary_key=True)
    ref_foto = models.CharField(max_length=255)

    def __str__(self):
        return f"Foto de {self.id_sendero.nombre_sendero}"


class RegistroVisita(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)
    razon_visita = models.TextField()
    sendero_visitado = models.TextField()
    fecha_visita = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visita de {self.visitante.nombre_visitante} a {self.sendero_visitado}"


class Encuesta(models.Model):
    visita = models.ForeignKey(RegistroVisita, on_delete=models.CASCADE)
    formulario = models.JSONField()

    def __str__(self):
        return f"Encuesta para visita {self.visita.id}"


class Usuario(models.Model):
    class Rol(models.TextChoices):
        ADMIN = "admin", "Administrador"
        USER = "user", "Usuario"

    email = CampoEncriptado(max_length=255)
    nombre = CampoEncriptado(max_length=255)
    apellido = CampoEncriptado(max_length=255)
    contraseña = models.CharField(max_length=255)  # Se almacena hasheada
    rol = models.CharField(max_length=5, choices=Rol.choices, default=Rol.USER)

    def save(self, *args, **kwargs):
        # Hashear contraseña solo si es nueva o modificada
        if not self.pk or 'contraseña' in self.get_dirty_fields():
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)

    def verificar_contraseña(self, contraseña_plana):
        """Verifica si la contraseña ingresada coincide con el hash"""
        return check_password(contraseña_plana, self.contraseña)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sendero = models.ForeignKey(Sendero, on_delete=models.CASCADE)
    foto_comentario = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.TextField()
    valoracion = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Comentario de {self.usuario.nombre} en {self.sendero.nombre_sendero}"
