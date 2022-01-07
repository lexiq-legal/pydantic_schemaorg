from pydantic import Field
from pydantic_schemaorg.BoatTerminal import BoatTerminal
from typing import List, Optional, Union
from pydantic_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See https://schema.org/BoatTrip.

    """
    type_: str = Field("BoatTrip", const=True, alias='@type')
    arrivalBoatTerminal: Optional[Union[List[Union[BoatTerminal, str]], Union[BoatTerminal, str]]] = Field(
        None,
        description="The terminal or port from which the boat arrives.",
    )
    departureBoatTerminal: Optional[Union[List[Union[BoatTerminal, str]], Union[BoatTerminal, str]]] = Field(
        None,
        description="The terminal or port from which the boat departs.",
    )
    

BoatTrip.update_forward_refs()
