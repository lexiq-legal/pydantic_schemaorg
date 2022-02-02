from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Boolean import Boolean


class True_(Boolean):
    """The boolean value true.

    See: https://schema.org/True
    Model depth: 6
    """
    type_: str = Field("True", alias='@type')
    

