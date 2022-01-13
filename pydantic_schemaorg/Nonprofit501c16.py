from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c16(USNonprofitType):
    """Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance"
     "Crop Operations.

    See: https://schema.org/Nonprofit501c16
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c16", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c16.update_forward_refs()
