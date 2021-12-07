from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraShort(WearableSizeGroupEnumeration):
    """Size group \"Extra Short\" for wearables.

    See https://schema.org/WearableSizeGroupExtraShort.

    """
    type_: str = Field("WearableSizeGroupExtraShort", const=True, alias='@type')
    

WearableSizeGroupExtraShort.update_forward_refs()
