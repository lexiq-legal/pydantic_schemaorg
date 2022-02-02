from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Neuro(PhysicalExam):
    """Neurological system clinical examination.

    See: https://schema.org/Neuro
    Model depth: 5
    """
    type_: str = Field("Neuro", alias='@type')
    

