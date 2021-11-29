from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """Enumerates common size systems for different categories of products, for example \"EN-13402\""
     "or \"UK\" for wearables or \"Imperial\" for screws.

    See https://schema.org/SizeSystemEnumeration.

    """

    locals().update({"@type": Field("SizeSystemEnumeration", const=True)})


SizeSystemEnumeration.update_forward_refs()
