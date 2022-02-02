from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class Flexibility(PhysicalActivityCategory):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    See: https://schema.org/Flexibility
    Model depth: 5
    """
    type_: str = Field("Flexibility", alias='@type')
    

