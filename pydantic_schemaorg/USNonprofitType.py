from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NonprofitType import NonprofitType


class USNonprofitType(NonprofitType):
    """USNonprofitType: Non-profit organization type originating from the United States.

    See: https://schema.org/USNonprofitType
    Model depth: 5
    """

    type_: str = Field("USNonprofitType", const=True, alias="@type")


if TYPE_CHECKING:

    USNonprofitType.update_forward_refs()
