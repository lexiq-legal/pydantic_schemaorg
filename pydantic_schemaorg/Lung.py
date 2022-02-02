from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Lung(PhysicalExam):
    """Lung and respiratory system clinical examination.

    See: https://schema.org/Lung
    Model depth: 5
    """
    type_: str = Field("Lung", alias='@type')
    

