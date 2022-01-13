from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c27(USNonprofitType):
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation"
     "Reinsurance Organizations.

    See: https://schema.org/Nonprofit501c27
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c27", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c27.update_forward_refs()
