from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemContinental(WearableSizeSystemEnumeration):
    """Continental size system for wearables.

    See https://schema.org/WearableSizeSystemContinental.

    """

    locals().update({"@type": Field("WearableSizeSystemContinental", const=True)})


WearableSizeSystemContinental.update_forward_refs()
