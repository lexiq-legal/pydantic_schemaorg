from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class ReturnFeesCustomerResponsibility(ReturnFeesEnumeration):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    See: https://schema.org/ReturnFeesCustomerResponsibility
    Model depth: 5
    """

    type_: str = Field("ReturnFeesCustomerResponsibility", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnFeesCustomerResponsibility.update_forward_refs()
