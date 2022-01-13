from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class OriginalShippingFees(ReturnFeesEnumeration):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    See: https://schema.org/OriginalShippingFees
    Model depth: 5
    """

    type_: str = Field("OriginalShippingFees", const=True, alias="@type")


if TYPE_CHECKING:

    OriginalShippingFees.update_forward_refs()
