from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c28(USNonprofitType):
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment"
     "Trusts.

    See: https://schema.org/Nonprofit501c28
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c28", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c28.update_forward_refs()
