from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Airport(CivicStructure):
    """An airport.

    See: https://schema.org/Airport
    Model depth: 4
    """
    type_: str = Field("Airport", alias='@type')
    iataCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="IATA identifier for an airline or airport.",
    )
    icaoCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="ICAO identifier for an airport.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
