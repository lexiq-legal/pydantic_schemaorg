from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import Any, Union, List, Optional
from datetime import datetime, time
from pydantic_schemaorg.Reservation import Reservation


class FoodEstablishmentReservation(Reservation):
    """A reservation to dine at a food-related business. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See https://schema.org/FoodEstablishmentReservation.

    """

    partySize: Optional[Union[List[Union[int, QuantitativeValue]], Union[int, QuantitativeValue]]] = Field(
        None,
        description="Number of people the reservation should accommodate.",
    )
    endTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    startTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. e.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    locals().update({"@type": Field("FoodEstablishmentReservation", const=True)})


FoodEstablishmentReservation.update_forward_refs()
