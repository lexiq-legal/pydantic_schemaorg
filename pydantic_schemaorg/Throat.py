from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Throat(PhysicalExam):
    """Throat assessment with clinical examination.

    See: https://schema.org/Throat
    Model depth: 5
    """
    type_: str = Field("Throat", alias='@type')
    

