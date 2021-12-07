from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    See https://schema.org/RoofingContractor.

    """
    type_: str = Field("RoofingContractor", const=True, alias='@type')
    

RoofingContractor.update_forward_refs()
