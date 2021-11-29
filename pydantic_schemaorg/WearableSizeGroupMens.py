from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMens(WearableSizeGroupEnumeration):
    """Size group \"Mens\" for wearables.

    See https://schema.org/WearableSizeGroupMens.

    """

    locals().update({"@type": Field("WearableSizeGroupMens", const=True)})


WearableSizeGroupMens.update_forward_refs()
