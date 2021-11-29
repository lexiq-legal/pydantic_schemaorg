from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationConfirmed(ReservationStatusType):
    """The status of a confirmed reservation.

    See https://schema.org/ReservationConfirmed.

    """

    locals().update({"@type": Field("ReservationConfirmed", const=True)})


ReservationConfirmed.update_forward_refs()
