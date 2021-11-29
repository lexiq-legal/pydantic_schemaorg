from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Trip import Trip


class BoatTrip(Trip):
    """A trip on a commercial ferry line.

    See https://schema.org/BoatTrip.

    """

    arrivalBoatTerminal: Any = Field(
        None,
        description="The terminal or port from which the boat arrives.",
    )
    departureBoatTerminal: Any = Field(
        None,
        description="The terminal or port from which the boat departs.",
    )
    locals().update({"@type": Field("BoatTrip", const=True)})


BoatTrip.update_forward_refs()
