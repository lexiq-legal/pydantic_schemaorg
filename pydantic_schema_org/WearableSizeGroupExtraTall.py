from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraTall(WearableSizeGroupEnumeration):
    """Size group \"Extra Tall\" for wearables.

    See https://schema.org/WearableSizeGroupExtraTall.

    """

    locals().update({"@type": Field("WearableSizeGroupExtraTall", const=True)})


WearableSizeGroupExtraTall.update_forward_refs()
