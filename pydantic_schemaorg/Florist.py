from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class Florist(Store):
    """A florist.

    See: https://schema.org/Florist
    Model depth: 5
    """
    type_: str = Field("Florist", alias='@type')
    

