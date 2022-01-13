from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class DisabilitySupport(GovernmentBenefitsType):
    """DisabilitySupport: this is a benefit for disability support.

    See: https://schema.org/DisabilitySupport
    Model depth: 5
    """

    type_: str = Field("DisabilitySupport", const=True, alias="@type")


if TYPE_CHECKING:

    DisabilitySupport.update_forward_refs()
