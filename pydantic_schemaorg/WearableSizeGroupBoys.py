from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBoys(WearableSizeGroupEnumeration):
    """Size group \"Boys\" for wearables.

    See https://schema.org/WearableSizeGroupBoys.

    """
    type_: str = Field("WearableSizeGroupBoys", const=True, alias='@type')
    

WearableSizeGroupBoys.update_forward_refs()
