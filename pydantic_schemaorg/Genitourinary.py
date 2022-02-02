from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Genitourinary(PhysicalExam):
    """Genitourinary system function assessment with clinical examination.

    See: https://schema.org/Genitourinary
    Model depth: 5
    """
    type_: str = Field("Genitourinary", alias='@type')
    

