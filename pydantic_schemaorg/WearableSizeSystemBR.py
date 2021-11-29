from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemBR(WearableSizeSystemEnumeration):
    """Brazilian size system for wearables.

    See https://schema.org/WearableSizeSystemBR.

    """

    locals().update({"@type": Field("WearableSizeSystemBR", const=True)})


WearableSizeSystemBR.update_forward_refs()
