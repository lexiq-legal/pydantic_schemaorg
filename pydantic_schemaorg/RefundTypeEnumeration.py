from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """Enumerates several kinds of product return refund types.

    See: https://schema.org/RefundTypeEnumeration
    Model depth: 4
    """

    type_: str = Field("RefundTypeEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    RefundTypeEnumeration.update_forward_refs()
