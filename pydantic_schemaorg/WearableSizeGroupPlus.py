from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPlus(WearableSizeGroupEnumeration):
    """Size group \"Plus\" for wearables.

    See https://schema.org/WearableSizeGroupPlus.

    """

    locals().update({"@type": Field("WearableSizeGroupPlus", const=True)})


WearableSizeGroupPlus.update_forward_refs()
