from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    See: https://schema.org/RealEstateAgent
    Model depth: 4
    """

    type_: str = Field("RealEstateAgent", const=True, alias="@type")


if TYPE_CHECKING:

    RealEstateAgent.update_forward_refs()
