from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemAU(WearableSizeSystemEnumeration):
    """Australian size system for wearables.

    See https://schema.org/WearableSizeSystemAU.

    """

    locals().update({"@type": Field("WearableSizeSystemAU", const=True)})


WearableSizeSystemAU.update_forward_refs()
