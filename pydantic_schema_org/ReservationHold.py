from pydantic import Field
from pydantic_schema_org.ReservationStatusType import ReservationStatusType


class ReservationHold(ReservationStatusType):
    """The status of a reservation on hold pending an update like credit card number or flight"
     "changes.

    See https://schema.org/ReservationHold.

    """

    locals().update({"@type": Field("ReservationHold", const=True)})


ReservationHold.update_forward_refs()
