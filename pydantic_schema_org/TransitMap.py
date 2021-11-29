from pydantic import Field
from pydantic_schema_org.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See https://schema.org/TransitMap.

    """

    locals().update({"@type": Field("TransitMap", const=True)})


TransitMap.update_forward_refs()
