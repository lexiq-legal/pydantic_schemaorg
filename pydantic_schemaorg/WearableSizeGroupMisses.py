from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMisses(WearableSizeGroupEnumeration):
    """Size group \"Misses\" (also known as \"Missy\") for wearables.

    See https://schema.org/WearableSizeGroupMisses.

    """
    type_: str = Field("WearableSizeGroupMisses", const=True, alias='@type')
    

WearableSizeGroupMisses.update_forward_refs()
