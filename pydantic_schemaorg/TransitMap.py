from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See https://schema.org/TransitMap.

    """
    type_: str = Field("TransitMap", const=True, alias='@type')
    

TransitMap.update_forward_refs()
