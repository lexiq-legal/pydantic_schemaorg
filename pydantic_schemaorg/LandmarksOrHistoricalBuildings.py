from pydantic import Field
from pydantic_schemaorg.Place import Place


class LandmarksOrHistoricalBuildings(Place):
    """An historical landmark or building.

    See https://schema.org/LandmarksOrHistoricalBuildings.

    """

    locals().update({"@type": Field("LandmarksOrHistoricalBuildings", const=True)})


LandmarksOrHistoricalBuildings.update_forward_refs()
