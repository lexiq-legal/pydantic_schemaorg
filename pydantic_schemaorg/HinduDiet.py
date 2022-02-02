from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HinduDiet(RestrictedDiet):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    See: https://schema.org/HinduDiet
    Model depth: 5
    """
    type_: str = Field("HinduDiet", alias='@type')
    

