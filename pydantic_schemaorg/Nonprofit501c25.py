from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c25(USNonprofitType):
    """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations"
     "or Trusts with Multiple Parents.

    See: https://schema.org/Nonprofit501c25
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c25", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c25.update_forward_refs()
