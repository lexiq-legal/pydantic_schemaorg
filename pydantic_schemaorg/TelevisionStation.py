from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station.

    See: https://schema.org/TelevisionStation
    Model depth: 4
    """

    type_: str = Field("TelevisionStation", const=True, alias="@type")


if TYPE_CHECKING:

    TelevisionStation.update_forward_refs()
