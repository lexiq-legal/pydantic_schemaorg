from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall.

    See: https://schema.org/CityHall
    Model depth: 5
    """
    type_: str = Field("CityHall", alias='@type')
    

