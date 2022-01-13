from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnNotPermitted(MerchantReturnEnumeration):
    """Specifies that product returns are not permitted.

    See: https://schema.org/MerchantReturnNotPermitted
    Model depth: 5
    """

    type_: str = Field("MerchantReturnNotPermitted", const=True, alias="@type")


if TYPE_CHECKING:

    MerchantReturnNotPermitted.update_forward_refs()
