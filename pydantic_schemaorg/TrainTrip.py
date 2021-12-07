from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Trip import Trip


class TrainTrip(Trip):
    """A trip on a commercial train line.

    See https://schema.org/TrainTrip.

    """
    type_: str = Field("TrainTrip", const=True, alias='@type')
    arrivalStation: Any = Field(
        None,
        description="The station where the train trip ends.",
    )
    departurePlatform: Optional[Union[List[str], str]] = Field(
        None,
        description="The platform from which the train departs.",
    )
    trainNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The unique identifier for the train.",
    )
    arrivalPlatform: Optional[Union[List[str], str]] = Field(
        None,
        description="The platform where the train arrives.",
    )
    trainName: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of the train (e.g. The Orient Express).",
    )
    departureStation: Any = Field(
        None,
        description="The station from which the train departs.",
    )
    

TrainTrip.update_forward_refs()
