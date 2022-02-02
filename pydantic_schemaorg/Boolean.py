from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class Boolean(DataType):
    """Boolean: True or False.

    See: https://schema.org/Boolean
    Model depth: 5
    """
    type_: str = Field("Boolean", alias='@type')
    

