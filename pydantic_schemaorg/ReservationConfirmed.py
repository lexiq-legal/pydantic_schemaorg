from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationConfirmed(ReservationStatusType):
    """The status of a confirmed reservation.

    See https://schema.org/ReservationConfirmed.

    """
    type_: str = Field("ReservationConfirmed", const=True, alias='@type')
    

ReservationConfirmed.update_forward_refs()
