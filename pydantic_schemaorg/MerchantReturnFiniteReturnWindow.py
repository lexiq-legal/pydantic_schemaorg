from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnFiniteReturnWindow(MerchantReturnEnumeration):
    """Specifies that there is a finite window for product returns.

    See: https://schema.org/MerchantReturnFiniteReturnWindow
    Model depth: 5
    """

    type_: str = Field("MerchantReturnFiniteReturnWindow", const=True, alias="@type")


if TYPE_CHECKING:

    MerchantReturnFiniteReturnWindow.update_forward_refs()
