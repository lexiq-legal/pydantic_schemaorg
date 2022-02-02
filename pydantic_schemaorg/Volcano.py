from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Volcano(Landform):
    """A volcano, like Fuji san.

    See: https://schema.org/Volcano
    Model depth: 4
    """
    type_: str = Field("Volcano", alias='@type')
    

