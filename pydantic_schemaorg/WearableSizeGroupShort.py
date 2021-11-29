from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupShort(WearableSizeGroupEnumeration):
    """Size group \"Short\" for wearables.

    See https://schema.org/WearableSizeGroupShort.

    """

    locals().update({"@type": Field("WearableSizeGroupShort", const=True)})


WearableSizeGroupShort.update_forward_refs()
