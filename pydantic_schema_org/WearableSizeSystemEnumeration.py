from pydantic import Field
from pydantic_schema_org.SizeSystemEnumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """Enumerates common size systems specific for wearable products

    See https://schema.org/WearableSizeSystemEnumeration.

    """

    locals().update({"@type": Field("WearableSizeSystemEnumeration", const=True)})


WearableSizeSystemEnumeration.update_forward_refs()
