from pydantic import Field
from pydantic_schemaorg.BusStop import BusStop
from pydantic_schemaorg.BusStation import BusStation
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Trip import Trip


class BusTrip(Trip):
    """A trip on a commercial bus line.

    See https://schema.org/BusTrip.

    """
    type_: str = Field("BusTrip", const=True, alias='@type')
    departureBusStop: Optional[Union[List[Union[BusStop, BusStation, str]], Union[BusStop, BusStation, str]]] = Field(
        None,
        description="The stop or station from which the bus departs.",
    )
    arrivalBusStop: Optional[Union[List[Union[BusStop, BusStation, str]], Union[BusStop, BusStation, str]]] = Field(
        None,
        description="The stop or station from which the bus arrives.",
    )
    busNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The unique identifier for the bus.",
    )
    busName: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of the bus (e.g. Bolt Express).",
    )
    

BusTrip.update_forward_refs()
