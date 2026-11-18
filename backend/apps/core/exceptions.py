"""Excepciones de dominio, mapeadas a respuestas 4xx/5xx con mensajes en español."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class DominioError(Exception):
    codigo_http = status.HTTP_400_BAD_REQUEST
    mensaje_por_defecto = "Operación no válida."

    def __init__(self, mensaje: str | None = None, **extra):
        self.mensaje = mensaje or self.mensaje_por_defecto
        self.extra = extra
        super().__init__(self.mensaje)


class ColaboradorNoEncontrado(DominioError):
    codigo_http = status.HTTP_400_BAD_REQUEST
    mensaje_por_defecto = "El colaborador no existe o no está activo. Verifique la identificación."


class TipoCasoNoReconocido(DominioError):
    mensaje_por_defecto = "Tipo de caso no reconocido: requiere clasificación manual (RN-004)."


class TransicionInvalida(DominioError):
    codigo_http = status.HTTP_409_CONFLICT
    mensaje_por_defecto = "La transición de estado solicitada no está permitida."


class DocumentoInvalido(DominioError):
    codigo_http = status.HTTP_422_UNPROCESSABLE_ENTITY
    mensaje_por_defecto = "Formato de archivo no válido: solo se admiten imágenes (JPG/PNG) o PDF."


class CasoBloqueado(DominioError):
    codigo_http = status.HTTP_409_CONFLICT
    mensaje_por_defecto = "El caso está bloqueado hasta resolver la inconsistencia (RF-008)."


class PlazoNoParametrizado(DominioError):
    mensaje_por_defecto = "La entidad no tiene plazo de transcripción parametrizado: defínalo manualmente (RN-007)."


class IAIndisponible(DominioError):
    codigo_http = status.HTTP_503_SERVICE_UNAVAILABLE
    mensaje_por_defecto = "El servicio de IA no está disponible. Continúe en modo de verificación manual."


class IARespuestaInvalida(DominioError):
    codigo_http = status.HTTP_502_BAD_GATEWAY
    mensaje_por_defecto = "La respuesta del servicio de IA no es válida."


def manejador_excepciones(exc, contexto):
    if isinstance(exc, DominioError):
        cuerpo = {"detalle": exc.mensaje, **exc.extra}
        if isinstance(exc, IAIndisponible):
            cuerpo["modo_manual"] = True
        return Response(cuerpo, status=exc.codigo_http)
    return exception_handler(exc, contexto)
