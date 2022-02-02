from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Boolean import Boolean


class False_(Boolean):
    """The boolean value false.

    See: https://schema.org/False
    Model depth: 6
    """
    type_: str = Field("False", alias='@type')
    

