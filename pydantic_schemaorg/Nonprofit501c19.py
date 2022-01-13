from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c19(USNonprofitType):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present"
     "Members of the Armed Forces.

    See: https://schema.org/Nonprofit501c19
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c19", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c19.update_forward_refs()
