from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class TrainReservation(Reservation):
    """A reservation for train travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See https://schema.org/TrainReservation.

    """
    type_: str = Field("TrainReservation", const=True, alias='@type')
    

TrainReservation.update_forward_refs()
