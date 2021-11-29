from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    See https://schema.org/LegislativeBuilding.

    """

    locals().update({"@type": Field("LegislativeBuilding", const=True)})


LegislativeBuilding.update_forward_refs()
