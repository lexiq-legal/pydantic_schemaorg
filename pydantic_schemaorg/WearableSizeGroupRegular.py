from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupRegular(WearableSizeGroupEnumeration):
    """Size group \"Regular\" for wearables.

    See https://schema.org/WearableSizeGroupRegular.

    """
    type_: str = Field("WearableSizeGroupRegular", const=True, alias='@type')
    

WearableSizeGroupRegular.update_forward_refs()
