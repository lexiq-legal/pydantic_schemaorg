from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class LowSaltDiet(RestrictedDiet):
    """A diet focused on reduced sodium intake.

    See: https://schema.org/LowSaltDiet
    Model depth: 5
    """
    type_: str = Field("LowSaltDiet", alias='@type')
    

