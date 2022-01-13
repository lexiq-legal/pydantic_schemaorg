from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class Map(CreativeWork):
    """A map.

    See: https://schema.org/Map
    Model depth: 3
    """

    type_: str = Field("Map", const=True, alias="@type")
    mapType: "Optional[Union[List[Union[MapCategoryType, str]], Union[MapCategoryType, str]]]" = Field(
        None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MapCategoryType import MapCategoryType

    Map.update_forward_refs()
