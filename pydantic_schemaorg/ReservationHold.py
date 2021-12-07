from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationHold(ReservationStatusType):
    """The status of a reservation on hold pending an update like credit card number or flight"
     "changes.

    See https://schema.org/ReservationHold.

    """
    type_: str = Field("ReservationHold", const=True, alias='@type')
    

ReservationHold.update_forward_refs()
