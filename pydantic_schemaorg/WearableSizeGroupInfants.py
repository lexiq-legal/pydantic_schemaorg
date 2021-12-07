from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupInfants(WearableSizeGroupEnumeration):
    """Size group \"Infants\" for wearables.

    See https://schema.org/WearableSizeGroupInfants.

    """
    type_: str = Field("WearableSizeGroupInfants", const=True, alias='@type')
    

WearableSizeGroupInfants.update_forward_refs()
