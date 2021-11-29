from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupRegular(WearableSizeGroupEnumeration):
    """Size group \"Regular\" for wearables.

    See https://schema.org/WearableSizeGroupRegular.

    """

    locals().update({"@type": Field("WearableSizeGroupRegular", const=True)})


WearableSizeGroupRegular.update_forward_refs()
