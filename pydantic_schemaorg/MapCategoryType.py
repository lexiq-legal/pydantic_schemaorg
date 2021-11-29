from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MapCategoryType(Enumeration):
    """An enumeration of several kinds of Map.

    See https://schema.org/MapCategoryType.

    """

    locals().update({"@type": Field("MapCategoryType", const=True)})


MapCategoryType.update_forward_refs()
