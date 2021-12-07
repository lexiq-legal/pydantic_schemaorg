from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMens(WearableSizeGroupEnumeration):
    """Size group \"Mens\" for wearables.

    See https://schema.org/WearableSizeGroupMens.

    """
    type_: str = Field("WearableSizeGroupMens", const=True, alias='@type')
    

WearableSizeGroupMens.update_forward_refs()
