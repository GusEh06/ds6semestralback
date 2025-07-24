from ..models import Comentario
from django.db.models import Avg

def obtener_valoracion_promedio(sendero_id):
    promedio = Comentario.objects.filter(sendero_id=sendero_id).aggregate(Avg('valoracion'))['valoracion__avg']
    if promedio is not None:
        return round(promedio, 1)
    return None

def obtener_valoraciones_por_sendero(sendero_id):
    comentarios = Comentario.objects.filter(sendero_id=sendero_id).select_related('usuario')
    return [
        {
            "usuario": f"{comentario.usuario.nombre} {comentario.usuario.apellido}",
            "valoracion": comentario.valoracion,
            "comentario": comentario.comentario
        }
        for comentario in comentarios
    ]

