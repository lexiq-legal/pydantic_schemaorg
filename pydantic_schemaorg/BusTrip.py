from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Trip import Trip


class BusTrip(Trip):
    """A trip on a commercial bus line.

    See: https://schema.org/BusTrip
    Model depth: 4
    """

    type_: str = Field("BusTrip", const=True, alias="@type")
    departureBusStop: "Optional[Union[List[Union[BusStop, BusStation, str]], Union[BusStop, BusStation, str]]]" = Field(
        None,
        description="The stop or station from which the bus departs.",
    )
    arrivalBusStop: "Optional[Union[List[Union[BusStop, BusStation, str]], Union[BusStop, BusStation, str]]]" = Field(
        None,
        description="The stop or station from which the bus arrives.",
    )
    busNumber: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The unique identifier for the bus.",
    )
    busName: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The name of the bus (e.g. Bolt Express).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.BusStop import BusStop

    from pydantic_schemaorg.BusStation import BusStation

    BusTrip.update_forward_refs()
