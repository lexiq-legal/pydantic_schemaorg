from pydantic import Field
from pydantic_schemaorg.MapCategoryType import MapCategoryType


class TransitMap(MapCategoryType):
    """A transit map.

    See https://schema.org/TransitMap.

    """

    locals().update({"@type": Field("TransitMap", const=True)})


TransitMap.update_forward_refs()
