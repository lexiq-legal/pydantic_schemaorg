from pydantic import Field
from pydantic_schema_org.ReservationStatusType import ReservationStatusType


class ReservationPending(ReservationStatusType):
    """The status of a reservation when a request has been sent, but not confirmed.

    See https://schema.org/ReservationPending.

    """

    locals().update({"@type": Field("ReservationPending", const=True)})


ReservationPending.update_forward_refs()
