from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupWomens(WearableSizeGroupEnumeration):
    """Size group \"Womens\" for wearables.

    See https://schema.org/WearableSizeGroupWomens.

    """
    type_: str = Field("WearableSizeGroupWomens", const=True, alias='@type')
    

WearableSizeGroupWomens.update_forward_refs()
