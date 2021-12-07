from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class SeatingMap(MapCategoryType):
    """A seating map.

    See https://schema.org/SeatingMap.

    """
    type_: str = Field("SeatingMap", const=True, alias='@type')
    

SeatingMap.update_forward_refs()
