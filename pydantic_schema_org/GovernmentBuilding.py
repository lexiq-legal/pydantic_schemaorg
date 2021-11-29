from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See https://schema.org/GovernmentBuilding.

    """

    locals().update({"@type": Field("GovernmentBuilding", const=True)})


GovernmentBuilding.update_forward_refs()
