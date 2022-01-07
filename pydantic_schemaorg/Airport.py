from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.CivicStructure import CivicStructure


class Airport(CivicStructure):
    """An airport.

    See https://schema.org/Airport.

    """
    type_: str = Field("Airport", const=True, alias='@type')
    iataCode: Optional[Union[List[str], str]] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    icaoCode: Optional[Union[List[str], str]] = Field(
        None,
        description="ICAO identifier for an airport.",
    )
    

Airport.update_forward_refs()
