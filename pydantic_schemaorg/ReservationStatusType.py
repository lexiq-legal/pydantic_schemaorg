from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """Enumerated status values for Reservation.

    See https://schema.org/ReservationStatusType.

    """
    type_: str = Field("ReservationStatusType", const=True, alias='@type')
    

ReservationStatusType.update_forward_refs()
