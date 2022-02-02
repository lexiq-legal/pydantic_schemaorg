from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationCancelled(ReservationStatusType):
    """The status for a previously confirmed reservation that is now cancelled.

    See: https://schema.org/ReservationCancelled
    Model depth: 6
    """
    type_: str = Field("ReservationCancelled", alias='@type')
    

