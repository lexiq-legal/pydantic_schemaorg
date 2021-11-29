from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.QualitativeValue import QualitativeValue
from pydantic_schema_org.Intangible import Intangible


class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    See https://schema.org/Seat.

    """

    seatNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The location of the reserved seat (e.g., 27).",
    )
    seatSection: Optional[Union[List[str], str]] = Field(
        None,
        description="The section location of the reserved seat (e.g. Orchestra).",
    )
    seatingType: Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]] = Field(
        None,
        description="The type/class of the seat.",
    )
    seatRow: Optional[Union[List[str], str]] = Field(
        None,
        description="The row location of the reserved seat (e.g., B).",
    )
    locals().update({"@type": Field("Seat", const=True)})


Seat.update_forward_refs()
