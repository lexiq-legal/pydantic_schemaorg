from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupJuniors(WearableSizeGroupEnumeration):
    """Size group \"Juniors\" for wearables.

    See https://schema.org/WearableSizeGroupJuniors.

    """
    type_: str = Field("WearableSizeGroupJuniors", const=True, alias='@type')
    

WearableSizeGroupJuniors.update_forward_refs()
