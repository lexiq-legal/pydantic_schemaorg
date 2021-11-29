from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class FreeReturn(ReturnFeesEnumeration):
    """Specifies that product returns are free of charge for the customer.

    See https://schema.org/FreeReturn.

    """

    locals().update({"@type": Field("FreeReturn", const=True)})


FreeReturn.update_forward_refs()
