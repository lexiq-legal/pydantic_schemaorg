from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class UnemploymentSupport(GovernmentBenefitsType):
    """UnemploymentSupport: this is a benefit for unemployment support.

    See: https://schema.org/UnemploymentSupport
    Model depth: 5
    """

    type_: str = Field("UnemploymentSupport", const=True, alias="@type")


if TYPE_CHECKING:

    UnemploymentSupport.update_forward_refs()
