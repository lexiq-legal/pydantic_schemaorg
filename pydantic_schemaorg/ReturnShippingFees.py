from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class ReturnShippingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay the return shipping costs when returning a product

    See: https://schema.org/ReturnShippingFees
    Model depth: 5
    """
    type_: str = Field("ReturnShippingFees", alias='@type')
    

