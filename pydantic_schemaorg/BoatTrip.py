from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See https://schema.org/BoatTrip.

    """
    type_: str = Field("BoatTrip", const=True, alias='@type')
    arrivalBoatTerminal: Any = Field(
        None,
        description="The terminal or port from which the boat arrives.",
    )
    departureBoatTerminal: Any = Field(
        None,
        description="The terminal or port from which the boat departs.",
    )
    

BoatTrip.update_forward_refs()
