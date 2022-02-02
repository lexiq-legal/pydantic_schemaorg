from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class HalalDiet(RestrictedDiet):
    """A diet conforming to Islamic dietary practices.

    See: https://schema.org/HalalDiet
    Model depth: 5
    """
    type_: str = Field("HalalDiet", alias='@type')
    

