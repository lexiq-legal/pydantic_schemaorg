from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Photograph(CreativeWork):
    """A photograph.

    See: https://schema.org/Photograph
    Model depth: 3
    """
    type_: str = Field("Photograph", alias='@type')
    

