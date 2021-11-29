from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMisses(WearableSizeGroupEnumeration):
    """Size group \"Misses\" (also known as \"Missy\") for wearables.

    See https://schema.org/WearableSizeGroupMisses.

    """

    locals().update({"@type": Field("WearableSizeGroupMisses", const=True)})


WearableSizeGroupMisses.update_forward_refs()
