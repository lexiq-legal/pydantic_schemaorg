from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    See: https://schema.org/GeneralContractor
    Model depth: 5
    """
    type_: str = Field("GeneralContractor", alias='@type')
    

