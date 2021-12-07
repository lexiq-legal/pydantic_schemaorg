from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    See https://schema.org/LegislativeBuilding.

    """
    type_: str = Field("LegislativeBuilding", const=True, alias='@type')
    

LegislativeBuilding.update_forward_refs()
