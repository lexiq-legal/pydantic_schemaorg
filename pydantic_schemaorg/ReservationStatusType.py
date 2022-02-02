from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """Enumerated status values for Reservation.

    See: https://schema.org/ReservationStatusType
    Model depth: 5
    """
    type_: str = Field("ReservationStatusType", alias='@type')
    

