from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceComponentTypeEnumeration import (
    PriceComponentTypeEnumeration,
)


class ActivationFee(PriceComponentTypeEnumeration):
    """Represents the activation fee part of the total price for an offered product, for example"
     "a cellphone contract.

    See: https://schema.org/ActivationFee
    Model depth: 5
    """

    type_: str = Field("ActivationFee", const=True, alias="@type")


if TYPE_CHECKING:

    ActivationFee.update_forward_refs()
