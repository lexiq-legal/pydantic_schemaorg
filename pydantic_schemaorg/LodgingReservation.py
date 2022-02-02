from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from datetime import time


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See: https://schema.org/LodgingReservation
    Model depth: 4
    """
    type_: str = Field("LodgingReservation", alias='@type')
    lodgingUnitDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A full description of the lodging unit.",
    )
    numChildren: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        None,
        description="The number of children staying in the unit.",
    )
    checkinTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The earliest someone may check into a lodging establishment.",
    )
    numAdults: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        None,
        description="The number of adults staying in the unit.",
    )
    checkoutTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', time, 'Time', str]], ISO8601Date, 'DateTime', time, 'Time', str]] = Field(
        None,
        description="The latest someone may check out of a lodging establishment.",
    )
    lodgingUnitType: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        None,
        description="Textual description of the unit type (including suite vs. room, size of bed, etc.).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
