from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationConfirmed(ReservationStatusType):
    """The status of a confirmed reservation.

    See: https://schema.org/ReservationConfirmed
    Model depth: 6
    """

    type_: str = Field("ReservationConfirmed", const=True, alias="@type")


if TYPE_CHECKING:

    ReservationConfirmed.update_forward_refs()
