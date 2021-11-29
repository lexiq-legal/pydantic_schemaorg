from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class ReturnFeesCustomerResponsibility(ReturnFeesEnumeration):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    See https://schema.org/ReturnFeesCustomerResponsibility.

    """

    locals().update({"@type": Field("ReturnFeesCustomerResponsibility", const=True)})


ReturnFeesCustomerResponsibility.update_forward_refs()
