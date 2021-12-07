from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """Enumerates several types of product return methods.

    See https://schema.org/ReturnMethodEnumeration.

    """
    type_: str = Field("ReturnMethodEnumeration", const=True, alias='@type')
    

ReturnMethodEnumeration.update_forward_refs()
