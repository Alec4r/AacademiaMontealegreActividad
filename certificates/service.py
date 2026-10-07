"""
Lógica para decidir y emitir certificados de los cursos de Academia Horizonte.

Caso ficticio para la activación del valor Quality de edunext.

Este módulo todavía no implementa la función `issue_certificate`: esa lógica
se agrega como funcionalidad nueva en la rama feature/certificados.
"""

# Nota mínima para aprobar un curso y recibir el certificado.
NOTA_MINIMA_APROBACION = 70

# Plantilla HTML de certificado según el idioma del curso.
TEMPLATES = {
    "es": "certificado_es.html",
    "en": "certificado_en.html",
}
