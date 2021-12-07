from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class RestockingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay a restocking fee when returning a product

    See https://schema.org/RestockingFees.

    """
    type_: str = Field("RestockingFees", const=True, alias='@type')
    

RestockingFees.update_forward_refs()
