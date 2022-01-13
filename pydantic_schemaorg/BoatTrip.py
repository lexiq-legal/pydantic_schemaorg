from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See: https://schema.org/BoatTrip
    Model depth: 4
    """

    type_: str = Field("BoatTrip", const=True, alias="@type")
    arrivalBoatTerminal: "Optional[Union[List[Union[BoatTerminal, str]], Union[BoatTerminal, str]]]" = Field(
        None,
        description="The terminal or port from which the boat arrives.",
    )
    departureBoatTerminal: "Optional[Union[List[Union[BoatTerminal, str]], Union[BoatTerminal, str]]]" = Field(
        None,
        description="The terminal or port from which the boat departs.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.BoatTerminal import BoatTerminal

    BoatTrip.update_forward_refs()
