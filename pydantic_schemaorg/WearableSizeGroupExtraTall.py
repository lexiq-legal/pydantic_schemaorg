from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraTall(WearableSizeGroupEnumeration):
    """Size group \"Extra Tall\" for wearables.

    See https://schema.org/WearableSizeGroupExtraTall.

    """
    type_: str = Field("WearableSizeGroupExtraTall", const=True, alias='@type')
    

WearableSizeGroupExtraTall.update_forward_refs()
