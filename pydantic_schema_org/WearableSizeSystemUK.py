from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemUK(WearableSizeSystemEnumeration):
    """United Kingdom size system for wearables.

    See https://schema.org/WearableSizeSystemUK.

    """

    locals().update({"@type": Field("WearableSizeSystemUK", const=True)})


WearableSizeSystemUK.update_forward_refs()
