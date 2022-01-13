from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c5(USNonprofitType):
    """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural"
     "Organizations.

    See: https://schema.org/Nonprofit501c5
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c5", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c5.update_forward_refs()
