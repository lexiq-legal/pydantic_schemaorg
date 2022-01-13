from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c10(USNonprofitType):
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.

    See: https://schema.org/Nonprofit501c10
    Model depth: 6
    """

    type_: str = Field("Nonprofit501c10", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501c10.update_forward_refs()
