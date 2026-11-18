"""Preparación de archivos para la IA con PyMuPDF/Pillow (sin binarios del sistema, RNF-011)."""

from __future__ import annotations

import io


def preparar_para_ia(contenido: bytes, mime_type: str, max_paginas: int = 3, max_lado: int = 2048) -> tuple[bytes, str]:
    """Devuelve (bytes, mime). PDF => primera(s) página(s) renderizadas a PNG; imagen => reescalada.

    Para simplificar el MVP se devuelve una sola imagen PNG (página 1) cuando el PDF tiene varias páginas
    y las demás se unen verticalmente. Mantener el límite de páginas y de tamaño.
    """
    from PIL import Image

    if mime_type == "application/pdf":
        import fitz  # PyMuPDF

        with fitz.open(stream=contenido, filetype="pdf") as doc:
            imagenes = []
            for pagina in list(doc)[:max_paginas]:
                pix = pagina.get_pixmap(dpi=150)
                imagenes.append(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
        ancho = max(i.width for i in imagenes)
        alto = sum(i.height for i in imagenes)
        lienzo = Image.new("RGB", (ancho, alto), "white")
        y = 0
        for img in imagenes:
            lienzo.paste(img, (0, y))
            y += img.height
        imagen = lienzo
    else:
        imagen = Image.open(io.BytesIO(contenido)).convert("RGB")

    imagen.thumbnail((max_lado, max_lado))
    salida = io.BytesIO()
    imagen.save(salida, format="PNG", optimize=True)
    return salida.getvalue(), "image/png"
