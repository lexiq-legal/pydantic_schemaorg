from pydantic import Field
from pydantic_schema_org.MapCategoryType import MapCategoryType


class VenueMap(MapCategoryType):
    """A venue map (e.g. for malls, auditoriums, museums, etc.).

    See https://schema.org/VenueMap.

    """

    locals().update({"@type": Field("VenueMap", const=True)})


VenueMap.update_forward_refs()
