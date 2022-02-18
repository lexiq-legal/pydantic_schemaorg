from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See: https://schema.org/BoatTrip
    Model depth: 4
    """
    type_: str = Field(default="BoatTrip", alias='@type', const=True)
    arrivalBoatTerminal: Optional[Union[List[Union['BoatTerminal', str]], 'BoatTerminal', str]] = Field(
        default=None,
        description="The terminal or port from which the boat arrives.",
    )
    departureBoatTerminal: Optional[Union[List[Union['BoatTerminal', str]], 'BoatTerminal', str]] = Field(
        default=None,
        description="The terminal or port from which the boat departs.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.BoatTerminal import BoatTerminal
