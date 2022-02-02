from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    See: https://schema.org/Seat
    Model depth: 3
    """
    type_: str = Field("Seat", alias='@type')
    seatNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The location of the reserved seat (e.g., 27).",
    )
    seatSection: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The section location of the reserved seat (e.g. Orchestra).",
    )
    seatingType: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        None,
        description="The type/class of the seat.",
    )
    seatRow: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The row location of the reserved seat (e.g., B).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
