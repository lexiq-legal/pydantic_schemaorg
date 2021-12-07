from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupHusky(WearableSizeGroupEnumeration):
    """Size group \"Husky\" (or \"Stocky\") for wearables.

    See https://schema.org/WearableSizeGroupHusky.

    """
    type_: str = Field("WearableSizeGroupHusky", const=True, alias='@type')
    

WearableSizeGroupHusky.update_forward_refs()
