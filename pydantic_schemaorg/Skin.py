from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Skin(PhysicalExam):
    """Skin assessment with clinical examination.

    See: https://schema.org/Skin
    Model depth: 5
    """
    type_: str = Field("Skin", alias='@type')
    

