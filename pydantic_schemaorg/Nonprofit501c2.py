from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c2(USNonprofitType):
    """Nonprofit501c2: Non-profit type referring to Title-holding Corporations for Exempt"
     "Organizations.

    See: https://schema.org/Nonprofit501c2
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c2", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c2.update_forward_refs()
