from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neck(PhysicalExam):
    """Neck assessment with clinical examination.

    See: https://schema.org/Neck
    Model depth: 5
    """
    type_: str = Field("Neck", alias='@type')
    

