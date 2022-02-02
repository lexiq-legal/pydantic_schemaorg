from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowCalorieDiet(RestrictedDiet):
    """A diet focused on reduced calorie intake.

    See: https://schema.org/LowCalorieDiet
    Model depth: 5
    """
    type_: str = Field("LowCalorieDiet", alias='@type')
    

