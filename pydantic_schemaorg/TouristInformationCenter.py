from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """A tourist information center.

    See: https://schema.org/TouristInformationCenter
    Model depth: 4
    """

    type_: str = Field("TouristInformationCenter", const=True, alias="@type")


if TYPE_CHECKING:

    TouristInformationCenter.update_forward_refs()
