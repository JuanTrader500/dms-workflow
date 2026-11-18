from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ["*"]
IA_PROVEEDOR = __import__("os").getenv("IA_PROVEEDOR", "fake")
