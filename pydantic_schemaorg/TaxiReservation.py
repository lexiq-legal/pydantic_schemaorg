from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from datetime import datetime
from pydantic_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See https://schema.org/TaxiReservation.

    """

    partySize: Union[List[Union[int, Any]], Union[int, Any]] = Field(
        None,
        description="Number of people the reservation should accommodate.",
    )
    pickupLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    pickupTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )
    locals().update({"@type": Field("TaxiReservation", const=True)})


TaxiReservation.update_forward_refs()
