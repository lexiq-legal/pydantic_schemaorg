from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency.

    See: https://schema.org/TravelAgency
    Model depth: 4
    """

    type_: str = Field("TravelAgency", const=True, alias="@type")


if TYPE_CHECKING:

    TravelAgency.update_forward_refs()
