from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraShort(WearableSizeGroupEnumeration):
    """Size group \"Extra Short\" for wearables.

    See https://schema.org/WearableSizeGroupExtraShort.

    """

    locals().update({"@type": Field("WearableSizeGroupExtraShort", const=True)})


WearableSizeGroupExtraShort.update_forward_refs()
