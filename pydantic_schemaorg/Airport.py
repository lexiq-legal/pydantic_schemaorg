from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CivicStructure import CivicStructure


class Airport(CivicStructure):
    """An airport.

    See https://schema.org/Airport.

    """

    iataCode: Optional[Union[List[str], str]] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    icaoCode: Optional[Union[List[str], str]] = Field(
        None,
        description="ICAO identifier for an airport.",
    )
    locals().update({"@type": Field("Airport", const=True)})


Airport.update_forward_refs()
