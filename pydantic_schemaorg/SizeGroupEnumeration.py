from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class SizeGroupEnumeration(Enumeration):
    """Enumerates common size groups for various product categories.

    See https://schema.org/SizeGroupEnumeration.

    """

    locals().update({"@type": Field("SizeGroupEnumeration", const=True)})


SizeGroupEnumeration.update_forward_refs()
