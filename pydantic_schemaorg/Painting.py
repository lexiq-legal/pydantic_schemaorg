from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Painting(CreativeWork):
    """A painting.

    See: https://schema.org/Painting
    Model depth: 3
    """
    type_: str = Field("Painting", alias='@type')
    

