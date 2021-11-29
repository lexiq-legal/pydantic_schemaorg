from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupJuniors(WearableSizeGroupEnumeration):
    """Size group \"Juniors\" for wearables.

    See https://schema.org/WearableSizeGroupJuniors.

    """

    locals().update({"@type": Field("WearableSizeGroupJuniors", const=True)})


WearableSizeGroupJuniors.update_forward_refs()
