from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support"
     "the COVID-19 situation. Note that this structure may not capture all benefits offered.

    See: https://schema.org/GovernmentBenefitsType
    Model depth: 4
    """

    type_: str = Field("GovernmentBenefitsType", const=True, alias="@type")


if TYPE_CHECKING:

    GovernmentBenefitsType.update_forward_refs()
