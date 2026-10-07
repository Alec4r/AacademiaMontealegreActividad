"""Tests de la lógica de emisión de certificados."""

import pytest

service = pytest.importorskip("certificates.service")


@pytest.mark.skipif(
    not hasattr(service, "issue_certificate"),
    reason="issue_certificate todavía no está implementada (ver rama feature/certificados)",
)
def test_student_with_70_gets_certificate():
    """
    Requisito de negocio: una nota igual o mayor a 70 aprueba el curso
    y debe recibir el certificado. Una nota de exactamente 70 es el caso
    límite que esta prueba protege.
    """
    student = {"name": "Ana Pérez", "grade": 70}
    course = {"name": "Introducción a Python", "language": "es"}

    assert service.issue_certificate(student, course) is True
