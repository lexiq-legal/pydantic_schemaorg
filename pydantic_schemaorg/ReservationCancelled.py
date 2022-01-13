from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReservationStatusType import ReservationStatusType


class ReservationCancelled(ReservationStatusType):
    """The status for a previously confirmed reservation that is now cancelled.

    See: https://schema.org/ReservationCancelled
    Model depth: 6
    """

    type_: str = Field("ReservationCancelled", const=True, alias="@type")


if TYPE_CHECKING:

    ReservationCancelled.update_forward_refs()
