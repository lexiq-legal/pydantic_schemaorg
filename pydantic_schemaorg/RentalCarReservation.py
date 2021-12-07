from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import Any, Optional, Union, List
from datetime import datetime
from pydantic_schemaorg.Reservation import Reservation


class RentalCarReservation(Reservation):
    """A reservation for a rental car. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    See https://schema.org/RentalCarReservation.

    """
    type_: str = Field("RentalCarReservation", const=True, alias='@type')
    pickupLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    dropoffLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="Where a rental car can be dropped off.",
    )
    pickupTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )
    dropoffTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="When a rental car can be dropped off.",
    )
    

RentalCarReservation.update_forward_refs()
