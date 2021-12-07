from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MapCategoryType(Enumeration):
    """An enumeration of several kinds of Map.

    See https://schema.org/MapCategoryType.

    """
    type_: str = Field("MapCategoryType", const=True, alias='@type')
    

MapCategoryType.update_forward_refs()
