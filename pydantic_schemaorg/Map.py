from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType
from typing import List, Optional, Union, Any
from pydantic_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See https://schema.org/Map.

    """

    mapType: Optional[Union[List[MapCategoryType], MapCategoryType]] = Field(
        None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )
    locals().update({"@type": Field("Map", const=True)})


Map.update_forward_refs()
