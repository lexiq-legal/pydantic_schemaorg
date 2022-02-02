from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Number import Number


class Integer(Number):
    """Data type: Integer.

    See: https://schema.org/Integer
    Model depth: 6
    """
    type_: str = Field("Integer", alias='@type')
    

