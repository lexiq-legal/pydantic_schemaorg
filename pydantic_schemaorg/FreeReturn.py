from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class FreeReturn(ReturnFeesEnumeration):
    """Specifies that product returns are free of charge for the customer.

    See https://schema.org/FreeReturn.

    """
    type_: str = Field("FreeReturn", const=True, alias='@type')
    

FreeReturn.update_forward_refs()
