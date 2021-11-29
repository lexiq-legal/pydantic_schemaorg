from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemUS(WearableSizeSystemEnumeration):
    """United States size system for wearables.

    See https://schema.org/WearableSizeSystemUS.

    """

    locals().update({"@type": Field("WearableSizeSystemUS", const=True)})


WearableSizeSystemUS.update_forward_refs()
