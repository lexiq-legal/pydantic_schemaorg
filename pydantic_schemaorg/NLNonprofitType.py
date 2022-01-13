from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NonprofitType import NonprofitType


class NLNonprofitType(NonprofitType):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    See: https://schema.org/NLNonprofitType
    Model depth: 5
    """

    type_: str = Field("NLNonprofitType", const=True, alias="@type")


if TYPE_CHECKING:

    NLNonprofitType.update_forward_refs()
