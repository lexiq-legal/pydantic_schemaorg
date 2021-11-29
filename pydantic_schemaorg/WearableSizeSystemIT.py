from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemIT(WearableSizeSystemEnumeration):
    """Italian size system for wearables.

    See https://schema.org/WearableSizeSystemIT.

    """

    locals().update({"@type": Field("WearableSizeSystemIT", const=True)})


WearableSizeSystemIT.update_forward_refs()
