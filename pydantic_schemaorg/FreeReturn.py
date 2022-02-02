from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class FreeReturn(ReturnFeesEnumeration):
    """Specifies that product returns are free of charge for the customer.

    See: https://schema.org/FreeReturn
    Model depth: 5
    """
    type_: str = Field("FreeReturn", alias='@type')
    

