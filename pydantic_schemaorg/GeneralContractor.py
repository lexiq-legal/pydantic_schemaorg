from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    See https://schema.org/GeneralContractor.

    """
    type_: str = Field("GeneralContractor", const=True, alias='@type')
    

GeneralContractor.update_forward_refs()
