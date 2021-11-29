from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall.

    See https://schema.org/CityHall.

    """

    locals().update({"@type": Field("CityHall", const=True)})


CityHall.update_forward_refs()
