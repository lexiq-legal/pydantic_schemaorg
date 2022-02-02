from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Trip import Trip


class BusTrip(Trip):
    """A trip on a commercial bus line.

    See: https://schema.org/BusTrip
    Model depth: 4
    """
    type_: str = Field("BusTrip", alias='@type')
    departureBusStop: Optional[Union[List[Union['BusStop', 'BusStation', str]], 'BusStop', 'BusStation', str]] = Field(
        None,
        description="The stop or station from which the bus departs.",
    )
    arrivalBusStop: Optional[Union[List[Union['BusStop', 'BusStation', str]], 'BusStop', 'BusStation', str]] = Field(
        None,
        description="The stop or station from which the bus arrives.",
    )
    busNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The unique identifier for the bus.",
    )
    busName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The name of the bus (e.g. Bolt Express).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BusStop import BusStop
    from pydantic_schemaorg.BusStation import BusStation
    from pydantic_schemaorg.Text import Text
