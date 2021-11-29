from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemCN(WearableSizeSystemEnumeration):
    """Chinese size system for wearables.

    See https://schema.org/WearableSizeSystemCN.

    """

    locals().update({"@type": Field("WearableSizeSystemCN", const=True)})


WearableSizeSystemCN.update_forward_refs()
