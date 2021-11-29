from pydantic import Field
from pydantic_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """Enumerates common size groups (also known as \"size types\") for wearable products.

    See https://schema.org/WearableSizeGroupEnumeration.

    """

    locals().update({"@type": Field("WearableSizeGroupEnumeration", const=True)})


WearableSizeGroupEnumeration.update_forward_refs()
