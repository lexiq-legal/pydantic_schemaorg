from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501f(USNonprofitType):
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

    See: https://schema.org/Nonprofit501f
    Model depth: 6
    """

    type_: str = Field("Nonprofit501f", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501f.update_forward_refs()
