from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationPending(ReservationStatusType):
    """The status of a reservation when a request has been sent, but not confirmed.

    See: https://schema.org/ReservationPending
    Model depth: 6
    """
    type_: str = Field("ReservationPending", alias='@type')
    

