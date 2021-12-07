from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBig(WearableSizeGroupEnumeration):
    """Size group \"Big\" for wearables.

    See https://schema.org/WearableSizeGroupBig.

    """
    type_: str = Field("WearableSizeGroupBig", const=True, alias='@type')
    

WearableSizeGroupBig.update_forward_refs()
