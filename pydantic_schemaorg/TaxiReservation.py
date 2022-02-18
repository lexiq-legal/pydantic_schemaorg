from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/TaxiReservation
    Model depth: 4
    """
    type_: str = Field(default="TaxiReservation", alias='@type', const=True)
    partySize: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        default=None,
        description="Number of people the reservation should accommodate.",
    )
    pickupLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    pickupTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.DateTime import DateTime
