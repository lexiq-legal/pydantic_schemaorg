from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationConfirmed(ReservationStatusType):
    """The status of a confirmed reservation.

    See: https://schema.org/ReservationConfirmed
    Model depth: 6
    """
    type_: str = Field("ReservationConfirmed", alias='@type')
    

