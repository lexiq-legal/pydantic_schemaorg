from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitANBI(NLNonprofitType):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    See: https://schema.org/NonprofitANBI
    Model depth: 6
    """

    type_: str = Field("NonprofitANBI", const=True, alias="@type")


if TYPE_CHECKING:

    NonprofitANBI.update_forward_refs()
