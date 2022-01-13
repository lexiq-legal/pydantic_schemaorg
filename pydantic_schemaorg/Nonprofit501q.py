from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501q(USNonprofitType):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    See: https://schema.org/Nonprofit501q
    Model depth: 6
    """

    type_: str = Field("Nonprofit501q", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501q.update_forward_refs()
