from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class AnaerobicActivity(PhysicalActivityCategory):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism"
     "of the body.

    See: https://schema.org/AnaerobicActivity
    Model depth: 5
    """
    type_: str = Field("AnaerobicActivity", alias='@type')
    

