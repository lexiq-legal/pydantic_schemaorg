from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall.

    See https://schema.org/CityHall.

    """
    type_: str = Field("CityHall", const=True, alias='@type')
    

CityHall.update_forward_refs()
