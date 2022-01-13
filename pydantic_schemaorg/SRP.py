from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SRP(PriceTypeEnumeration):
    """Represents the suggested retail price (\"SRP\") of an offered product.

    See: https://schema.org/SRP
    Model depth: 5
    """

    type_: str = Field("SRP", const=True, alias="@type")


if TYPE_CHECKING:

    SRP.update_forward_refs()
