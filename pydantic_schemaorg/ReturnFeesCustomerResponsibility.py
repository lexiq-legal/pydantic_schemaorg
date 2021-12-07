from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class ReturnFeesCustomerResponsibility(ReturnFeesEnumeration):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    See https://schema.org/ReturnFeesCustomerResponsibility.

    """
    type_: str = Field("ReturnFeesCustomerResponsibility", const=True, alias='@type')
    

ReturnFeesCustomerResponsibility.update_forward_refs()
