from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class Text(DataType):
    """Data type: Text.

    See: https://schema.org/Text
    Model depth: 5
    """
    type_: str = Field(default="Text", alias='@type', const=True)
    
