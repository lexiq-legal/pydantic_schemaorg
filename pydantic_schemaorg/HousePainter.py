from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    See https://schema.org/HousePainter.

    """
    type_: str = Field("HousePainter", const=True, alias='@type')
    

HousePainter.update_forward_refs()
