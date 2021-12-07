from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    See https://schema.org/Locksmith.

    """
    type_: str = Field("Locksmith", const=True, alias='@type')
    

Locksmith.update_forward_refs()
