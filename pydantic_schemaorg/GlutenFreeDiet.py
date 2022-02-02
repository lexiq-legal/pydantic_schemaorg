from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class GlutenFreeDiet(RestrictedDiet):
    """A diet exclusive of gluten.

    See: https://schema.org/GlutenFreeDiet
    Model depth: 5
    """
    type_: str = Field("GlutenFreeDiet", alias='@type')
    

