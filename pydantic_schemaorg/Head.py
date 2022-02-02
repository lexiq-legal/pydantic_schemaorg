from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Head(PhysicalExam):
    """Head assessment with clinical examination.

    See: https://schema.org/Head
    Model depth: 5
    """
    type_: str = Field("Head", alias='@type')
    

