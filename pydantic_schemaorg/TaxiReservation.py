from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/TaxiReservation
    Model depth: 4
    """
    type_: str = Field("TaxiReservation", alias='@type')
    partySize: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        None,
        description="Number of people the reservation should accommodate.",
    )
    pickupLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    pickupTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.DateTime import DateTime
