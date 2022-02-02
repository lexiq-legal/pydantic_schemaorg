from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet


class DiabeticDiet(RestrictedDiet):
    """A diet appropriate for people with diabetes.

    See: https://schema.org/DiabeticDiet
    Model depth: 5
    """
    type_: str = Field("DiabeticDiet", alias='@type')
    

