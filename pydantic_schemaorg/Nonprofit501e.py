from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501e(USNonprofitType):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    See: https://schema.org/Nonprofit501e
    Model depth: 6
    """

    type_: str = Field("Nonprofit501e", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501e.update_forward_refs()
