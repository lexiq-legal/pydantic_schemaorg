from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitSBBI(NLNonprofitType):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution"
     "(NL).

    See: https://schema.org/NonprofitSBBI
    Model depth: 6
    """

    type_: str = Field("NonprofitSBBI", const=True, alias="@type")


if TYPE_CHECKING:

    NonprofitSBBI.update_forward_refs()
