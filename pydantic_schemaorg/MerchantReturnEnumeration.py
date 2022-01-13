from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """Enumerates several kinds of product return policies.

    See: https://schema.org/MerchantReturnEnumeration
    Model depth: 4
    """

    type_: str = Field("MerchantReturnEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    MerchantReturnEnumeration.update_forward_refs()
