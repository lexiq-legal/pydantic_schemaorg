from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class PaidLeave(GovernmentBenefitsType):
    """PaidLeave: this is a benefit for paid leave.

    See: https://schema.org/PaidLeave
    Model depth: 5
    """

    type_: str = Field("PaidLeave", const=True, alias="@type")


if TYPE_CHECKING:

    PaidLeave.update_forward_refs()
