from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Church import Church


class CatholicChurch(Church):
    """A Catholic church.

    See: https://schema.org/CatholicChurch
    Model depth: 6
    """
    type_: str = Field(default="CatholicChurch", alias='@type', const=True)
    
