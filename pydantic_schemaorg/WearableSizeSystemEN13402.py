from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemEN13402(WearableSizeSystemEnumeration):
    """EN 13402 (joint European standard for size labelling of clothes).

    See https://schema.org/WearableSizeSystemEN13402.

    """
    type_: str = Field("WearableSizeSystemEN13402", const=True, alias='@type')
    

WearableSizeSystemEN13402.update_forward_refs()
