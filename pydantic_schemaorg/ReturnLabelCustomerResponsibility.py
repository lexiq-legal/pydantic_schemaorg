from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelCustomerResponsibility(ReturnLabelSourceEnumeration):
    """Indicated that creating a return label is the responsibility of the customer.

    See: https://schema.org/ReturnLabelCustomerResponsibility
    Model depth: 5
    """

    type_: str = Field("ReturnLabelCustomerResponsibility", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnLabelCustomerResponsibility.update_forward_refs()
