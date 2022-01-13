from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/TaxiReservation
    Model depth: 4
    """

    type_: str = Field("TaxiReservation", const=True, alias="@type")
    partySize: "Optional[Union[List[Union[int, QuantitativeValue, str]], Union[int, QuantitativeValue, str]]]" = Field(
        None,
        description="Number of people the reservation should accommodate.",
    )
    pickupLocation: "Optional[Union[List[Union[Place, str]], Union[Place, str]]]" = Field(
        None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    pickupTime: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="When a taxi will pickup a passenger or a rental car can be picked up.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from pydantic_schemaorg.Place import Place

    from datetime import datetime

    TaxiReservation.update_forward_refs()
