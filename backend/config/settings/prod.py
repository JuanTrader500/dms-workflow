from .base import *  # noqa: F401,F403

DEBUG = False
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# TLS 1.2+ se termina en el proxy/balanceador de despliegue (RNF-001). Si hay proxy HTTPS:
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
