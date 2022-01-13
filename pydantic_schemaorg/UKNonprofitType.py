from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NonprofitType import NonprofitType


class UKNonprofitType(NonprofitType):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    See: https://schema.org/UKNonprofitType
    Model depth: 5
    """

    type_: str = Field("UKNonprofitType", const=True, alias="@type")


if TYPE_CHECKING:

    UKNonprofitType.update_forward_refs()
