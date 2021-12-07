from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    See https://schema.org/MovingCompany.

    """
    type_: str = Field("MovingCompany", const=True, alias='@type')
    

MovingCompany.update_forward_refs()
