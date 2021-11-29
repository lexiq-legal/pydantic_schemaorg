from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See https://schema.org/GovernmentBuilding.

    """

    locals().update({"@type": Field("GovernmentBuilding", const=True)})


GovernmentBuilding.update_forward_refs()
