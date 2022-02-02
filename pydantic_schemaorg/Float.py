from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Number import Number


class Float(Number):
    """Data type: Floating number.

    See: https://schema.org/Float
    Model depth: 6
    """
    type_: str = Field("Float", alias='@type')
    

