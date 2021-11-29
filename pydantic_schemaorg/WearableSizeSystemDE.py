from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemDE(WearableSizeSystemEnumeration):
    """German size system for wearables.

    See https://schema.org/WearableSizeSystemDE.

    """

    locals().update({"@type": Field("WearableSizeSystemDE", const=True)})


WearableSizeSystemDE.update_forward_refs()
