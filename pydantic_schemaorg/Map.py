from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See: https://schema.org/Map
    Model depth: 3
    """
    type_: str = Field("Map", alias='@type')
    mapType: Optional[Union[List[Union['MapCategoryType', str]], 'MapCategoryType', str]] = Field(
        None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MapCategoryType import MapCategoryType
