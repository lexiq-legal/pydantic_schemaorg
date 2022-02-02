from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class VeganDiet(RestrictedDiet):
    """A diet exclusive of all animal products.

    See: https://schema.org/VeganDiet
    Model depth: 5
    """
    type_: str = Field("VeganDiet", alias='@type')
    

