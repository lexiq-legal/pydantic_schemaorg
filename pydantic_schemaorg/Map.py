from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See https://schema.org/Map.

    """
    type_: str = Field("Map", const=True, alias='@type')
    mapType: Optional[Union[List[MapCategoryType], MapCategoryType]] = Field(
        None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )
    

Map.update_forward_refs()
