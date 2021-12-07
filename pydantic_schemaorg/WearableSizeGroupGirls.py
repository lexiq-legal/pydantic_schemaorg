from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupGirls(WearableSizeGroupEnumeration):
    """Size group \"Girls\" for wearables.

    See https://schema.org/WearableSizeGroupGirls.

    """
    type_: str = Field("WearableSizeGroupGirls", const=True, alias='@type')
    

WearableSizeGroupGirls.update_forward_refs()
