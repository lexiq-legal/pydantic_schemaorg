from pydantic import Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.Organization import Organization


class Airline(Organization):
    """An organization that provides flights for passengers.

    See https://schema.org/Airline.

    """

    boardingPolicy: Any = Field(
        None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    iataCode: Optional[Union[List[str], str]] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    locals().update({"@type": Field("Airline", const=True)})


Airline.update_forward_refs()
