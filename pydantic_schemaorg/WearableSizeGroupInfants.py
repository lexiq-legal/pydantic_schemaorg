from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupInfants(WearableSizeGroupEnumeration):
    """Size group \"Infants\" for wearables.

    See https://schema.org/WearableSizeGroupInfants.

    """

    locals().update({"@type": Field("WearableSizeGroupInfants", const=True)})


WearableSizeGroupInfants.update_forward_refs()
