from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Abdomen(PhysicalExam):
    """Abdomen clinical examination.

    See: https://schema.org/Abdomen
    Model depth: 5
    """
    type_: str = Field("Abdomen", alias='@type')
    

