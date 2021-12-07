from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    See https://schema.org/Electrician.

    """
    type_: str = Field("Electrician", const=True, alias='@type')
    

Electrician.update_forward_refs()
