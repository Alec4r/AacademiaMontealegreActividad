"""
Lógica para decidir y emitir certificados de los cursos de Academia Horizonte.

Caso ficticio para la activación del valor Quality de edunext.
"""

# Nota mínima para aprobar un curso y recibir el certificado.
NOTA_MINIMA_APROBACION = 70

# Plantilla HTML de certificado según el idioma del curso.
TEMPLATES = {
    "es": "certificado_es.html",
    "en": "certificado_en.html",
}


def issue_certificate(student, course):
    """
    Decide si el estudiante aprueba el curso y, si corresponde, envía
    (de forma simulada) el certificado en el idioma del curso.

    student: dict con al menos {"name": str, "grade": int|float}
    course: dict con al menos {"name": str, "language": "es"|"en"}

    Retorna True si se emitió el certificado, False si no.
    """
    grade = student["grade"]

    if grade > 70:
        _send_certificate(student, course)
        return True

    print(
        f"[certificados] {student['name']} no alcanzó la nota mínima "
        f"en {course['name']} (nota: {grade})."
    )
    return False


def _send_certificate(student, course):
    """Simula el envío del certificado (en un caso real, aquí se generaría el PDF/email)."""
    template = TEMPLATES["es"]
    print(
        f"[certificados] Enviando '{template}' a {student['name']} "
        f"por completar {course['name']}."
    )
