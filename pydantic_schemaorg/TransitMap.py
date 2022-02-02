from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See: https://schema.org/TransitMap
    Model depth: 5
    """
    type_: str = Field("TransitMap", alias='@type')
    

