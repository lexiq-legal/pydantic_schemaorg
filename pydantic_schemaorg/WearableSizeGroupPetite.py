from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPetite(WearableSizeGroupEnumeration):
    """Size group \"Petite\" for wearables.

    See https://schema.org/WearableSizeGroupPetite.

    """
    type_: str = Field("WearableSizeGroupPetite", const=True, alias='@type')
    

WearableSizeGroupPetite.update_forward_refs()
