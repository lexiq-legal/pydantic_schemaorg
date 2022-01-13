from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c7(USNonprofitType):
    """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.

    See: https://schema.org/Nonprofit501c7
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c7", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c7.update_forward_refs()
