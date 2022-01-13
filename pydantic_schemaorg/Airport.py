from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CivicStructure import CivicStructure


class Airport(CivicStructure):
    """An airport.

    See: https://schema.org/Airport
    Model depth: 4
    """

    type_: str = Field("Airport", const=True, alias="@type")
    iataCode: "Optional[Union[List[str], str]]" = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    icaoCode: "Optional[Union[List[str], str]]" = Field(
        None,
        description="ICAO identifier for an airport.",
    )


if TYPE_CHECKING:

    Airport.update_forward_refs()
