from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class ReservationPackage(Reservation):
    """A group of multiple reservations with common values for all sub-reservations.

    See: https://schema.org/ReservationPackage
    Model depth: 4
    """
    type_: str = Field("ReservationPackage", alias='@type')
    subReservation: Optional[Union[List[Union['Reservation', str]], 'Reservation', str]] = Field(
        None,
        description="The individual reservations included in the package. Typically a repeated property.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Reservation import Reservation
