from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class BoatReservation(Reservation):
    """A reservation for boat travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See https://schema.org/BoatReservation.

    """
    type_: str = Field("BoatReservation", const=True, alias='@type')
    

BoatReservation.update_forward_refs()
