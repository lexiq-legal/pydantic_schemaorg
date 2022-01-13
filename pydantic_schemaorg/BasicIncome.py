from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BasicIncome(GovernmentBenefitsType):
    """BasicIncome: this is a benefit for basic income.

    See: https://schema.org/BasicIncome
    Model depth: 5
    """

    type_: str = Field("BasicIncome", const=True, alias="@type")


if TYPE_CHECKING:

    BasicIncome.update_forward_refs()
