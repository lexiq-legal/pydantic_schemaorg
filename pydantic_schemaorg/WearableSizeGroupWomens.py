from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupWomens(WearableSizeGroupEnumeration):
    """Size group \"Womens\" for wearables.

    See https://schema.org/WearableSizeGroupWomens.

    """

    locals().update({"@type": Field("WearableSizeGroupWomens", const=True)})


WearableSizeGroupWomens.update_forward_refs()
