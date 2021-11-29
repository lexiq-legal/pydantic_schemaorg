from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemGS1(WearableSizeSystemEnumeration):
    """GS1 (formerly NRF) size system for wearables.

    See https://schema.org/WearableSizeSystemGS1.

    """

    locals().update({"@type": Field("WearableSizeSystemGS1", const=True)})


WearableSizeSystemGS1.update_forward_refs()
