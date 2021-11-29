from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupHusky(WearableSizeGroupEnumeration):
    """Size group \"Husky\" (or \"Stocky\") for wearables.

    See https://schema.org/WearableSizeGroupHusky.

    """

    locals().update({"@type": Field("WearableSizeGroupHusky", const=True)})


WearableSizeGroupHusky.update_forward_refs()
