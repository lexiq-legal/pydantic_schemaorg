from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c9(USNonprofitType):
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.

    See: https://schema.org/Nonprofit501c9
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c9", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c9.update_forward_refs()
