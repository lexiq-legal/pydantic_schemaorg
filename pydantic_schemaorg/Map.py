from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType
from typing import List, Optional, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See https://schema.org/Map.

    """
    type_: str = Field("Map", const=True, alias='@type')
    mapType: Optional[Union[List[Union[MapCategoryType, str]], Union[MapCategoryType, str]]] = Field(
        None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )
    

Map.update_forward_refs()
