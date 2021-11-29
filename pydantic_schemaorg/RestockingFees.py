from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class RestockingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay a restocking fee when returning a product

    See https://schema.org/RestockingFees.

    """

    locals().update({"@type": Field("RestockingFees", const=True)})


RestockingFees.update_forward_refs()
