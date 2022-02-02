from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Appearance(PhysicalExam):
    """Appearance assessment with clinical examination.

    See: https://schema.org/Appearance
    Model depth: 5
    """
    type_: str = Field("Appearance", alias='@type')
    

