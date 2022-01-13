from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station.

    See: https://schema.org/RadioStation
    Model depth: 4
    """

    type_: str = Field("RadioStation", const=True, alias="@type")


if TYPE_CHECKING:

    RadioStation.update_forward_refs()
