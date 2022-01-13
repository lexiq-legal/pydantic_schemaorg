from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See: https://schema.org/MerchantReturnUnspecified
    Model depth: 5
    """

    type_: str = Field("MerchantReturnUnspecified", const=True, alias="@type")


if TYPE_CHECKING:

    MerchantReturnUnspecified.update_forward_refs()
