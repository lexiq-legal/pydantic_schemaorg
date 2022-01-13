from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    See: https://schema.org/Seat
    Model depth: 3
    """

    type_: str = Field("Seat", const=True, alias="@type")
    seatNumber: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The location of the reserved seat (e.g., 27).",
    )
    seatSection: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The section location of the reserved seat (e.g. Orchestra).",
    )
    seatingType: "Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]]" = Field(
        None,
        description="The type/class of the seat.",
    )
    seatRow: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The row location of the reserved seat (e.g., B).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QualitativeValue import QualitativeValue

    Seat.update_forward_refs()
