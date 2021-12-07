from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class VenueMap(MapCategoryType):
    """A venue map (e.g. for malls, auditoriums, museums, etc.).

    See https://schema.org/VenueMap.

    """
    type_: str = Field("VenueMap", const=True, alias='@type')
    

VenueMap.update_forward_refs()
