from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class OriginalShippingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    See https://schema.org/OriginalShippingFees.

    """
    type_: str = Field("OriginalShippingFees", const=True, alias='@type')
    

OriginalShippingFees.update_forward_refs()
