from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMaternity(WearableSizeGroupEnumeration):
    """Size group \"Maternity\" for wearables.

    See https://schema.org/WearableSizeGroupMaternity.

    """
    type_: str = Field("WearableSizeGroupMaternity", const=True, alias='@type')
    

WearableSizeGroupMaternity.update_forward_refs()
