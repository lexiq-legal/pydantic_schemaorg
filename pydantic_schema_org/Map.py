from pydantic import Field
from pydantic_schema_org.MapCategoryType import MapCategoryType
from typing import Any, Optional, Union, List
from pydantic_schema_org.CreativeWork import CreativeWork


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
