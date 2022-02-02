from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowLactoseDiet(RestrictedDiet):
    """A diet appropriate for people with lactose intolerance.

    See: https://schema.org/LowLactoseDiet
    Model depth: 5
    """
    type_: str = Field("LowLactoseDiet", alias='@type')
    

