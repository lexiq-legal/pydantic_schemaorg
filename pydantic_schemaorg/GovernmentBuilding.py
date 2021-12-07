from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See https://schema.org/GovernmentBuilding.

    """
    type_: str = Field("GovernmentBuilding", const=True, alias='@type')
    

GovernmentBuilding.update_forward_refs()
