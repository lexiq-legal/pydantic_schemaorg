from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPetite(WearableSizeGroupEnumeration):
    """Size group \"Petite\" for wearables.

    See https://schema.org/WearableSizeGroupPetite.

    """

    locals().update({"@type": Field("WearableSizeGroupPetite", const=True)})


WearableSizeGroupPetite.update_forward_refs()
