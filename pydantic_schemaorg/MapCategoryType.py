from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MapCategoryType(Enumeration):
    """An enumeration of several kinds of Map.

    See: https://schema.org/MapCategoryType
    Model depth: 4
    """
    type_: str = Field("MapCategoryType", alias='@type')
    

