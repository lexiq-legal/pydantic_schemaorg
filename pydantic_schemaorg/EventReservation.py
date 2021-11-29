from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class EventReservation(Reservation):
    """A reservation for an event like a concert, sporting event, or lecture. Note: This type"
     "is for information about actual reservations, e.g. in confirmation emails or HTML pages"
     "with individual confirmations of reservations. For offers of tickets, use [[Offer]].

    See https://schema.org/EventReservation.

    """

    locals().update({"@type": Field("EventReservation", const=True)})


EventReservation.update_forward_refs()
