from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class SportsActivityLocation(LocalBusiness):
    """A sports location, such as a playing field.

    See: https://schema.org/SportsActivityLocation
    Model depth: 4
    """

    type_: str = Field("SportsActivityLocation", const=True, alias="@type")


if TYPE_CHECKING:

    SportsActivityLocation.update_forward_refs()
