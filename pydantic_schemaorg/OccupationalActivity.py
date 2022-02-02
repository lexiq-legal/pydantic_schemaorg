from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class OccupationalActivity(PhysicalActivityCategory):
    """Any physical activity engaged in for job-related purposes. Examples may include waiting"
     "tables, maid service, carrying a mailbag, picking fruits or vegetables, construction"
     "work, etc.

    See: https://schema.org/OccupationalActivity
    Model depth: 5
    """
    type_: str = Field("OccupationalActivity", alias='@type')
    

