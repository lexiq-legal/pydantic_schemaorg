from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    See: https://schema.org/RoofingContractor
    Model depth: 5
    """
    type_: str = Field("RoofingContractor", alias='@type')
    

