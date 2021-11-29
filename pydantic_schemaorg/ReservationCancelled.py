from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationCancelled(ReservationStatusType):
    """The status for a previously confirmed reservation that is now cancelled.

    See https://schema.org/ReservationCancelled.

    """

    locals().update({"@type": Field("ReservationCancelled", const=True)})


ReservationCancelled.update_forward_refs()
