from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture.

    See: https://schema.org/Sculpture
    Model depth: 3
    """
    type_: str = Field("Sculpture", alias='@type')
    

