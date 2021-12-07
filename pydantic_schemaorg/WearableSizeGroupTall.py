from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupTall(WearableSizeGroupEnumeration):
    """Size group \"Tall\" for wearables.

    See https://schema.org/WearableSizeGroupTall.

    """
    type_: str = Field("WearableSizeGroupTall", const=True, alias='@type')
    

WearableSizeGroupTall.update_forward_refs()
