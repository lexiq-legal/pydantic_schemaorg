from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """Enumerates common size systems for different categories of products, for example \"EN-13402\""
     "or \"UK\" for wearables or \"Imperial\" for screws.

    See https://schema.org/SizeSystemEnumeration.

    """
    type_: str = Field("SizeSystemEnumeration", const=True, alias='@type')
    

SizeSystemEnumeration.update_forward_refs()
