from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemFR(WearableSizeSystemEnumeration):
    """French size system for wearables.

    See https://schema.org/WearableSizeSystemFR.

    """

    locals().update({"@type": Field("WearableSizeSystemFR", const=True)})


WearableSizeSystemFR.update_forward_refs()
