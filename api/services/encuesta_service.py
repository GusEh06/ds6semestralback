from ..models import Encuesta, RegistroVisita

def registrar_encuesta(data):
    id_visita = data.get('id_visita')
    formulario = data.get('formulario')

    if not id_visita or not formulario:
        return None, "Datos incompletos"

    try:
        visita = RegistroVisita.objects.get(pk=id_visita)
    except RegistroVisita.DoesNotExist:
        return None, "La visita no existe"

    encuesta = Encuesta.objects.create(visita=visita, formulario=formulario)
    return encuesta, None
