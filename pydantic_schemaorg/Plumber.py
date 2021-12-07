from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """A plumbing service.

    See https://schema.org/Plumber.

    """
    type_: str = Field("Plumber", const=True, alias='@type')
    

Plumber.update_forward_refs()
