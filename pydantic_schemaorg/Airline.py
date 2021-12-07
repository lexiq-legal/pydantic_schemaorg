from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Organization import Organization


class Airline(Organization):
    """An organization that provides flights for passengers.

    See https://schema.org/Airline.

    """
    type_: str = Field("Airline", const=True, alias='@type')
    boardingPolicy: Any = Field(
        None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    iataCode: Optional[Union[List[str], str]] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    

Airline.update_forward_refs()
