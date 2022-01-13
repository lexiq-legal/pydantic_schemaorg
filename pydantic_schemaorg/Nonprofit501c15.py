from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c15(USNonprofitType):
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.

    See: https://schema.org/Nonprofit501c15
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c15", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c15.update_forward_refs()
