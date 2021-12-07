from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """Enumerates several kinds of policies for product return fees.

    See https://schema.org/ReturnFeesEnumeration.

    """
    type_: str = Field("ReturnFeesEnumeration", const=True, alias='@type')
    

ReturnFeesEnumeration.update_forward_refs()
