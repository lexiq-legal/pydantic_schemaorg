from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBoys(WearableSizeGroupEnumeration):
    """Size group \"Boys\" for wearables.

    See https://schema.org/WearableSizeGroupBoys.

    """

    locals().update({"@type": Field("WearableSizeGroupBoys", const=True)})


WearableSizeGroupBoys.update_forward_refs()
