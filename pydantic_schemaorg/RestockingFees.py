from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class RestockingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay a restocking fee when returning a product

    See: https://schema.org/RestockingFees
    Model depth: 5
    """
    type_: str = Field("RestockingFees", alias='@type')
    

