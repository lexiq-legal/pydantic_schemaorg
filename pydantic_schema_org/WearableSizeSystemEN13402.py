from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemEN13402(WearableSizeSystemEnumeration):
    """EN 13402 (joint European standard for size labelling of clothes).

    See https://schema.org/WearableSizeSystemEN13402.

    """

    locals().update({"@type": Field("WearableSizeSystemEN13402", const=True)})


WearableSizeSystemEN13402.update_forward_refs()
