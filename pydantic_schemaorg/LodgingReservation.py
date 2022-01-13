from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Reservation import Reservation


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See: https://schema.org/LodgingReservation
    Model depth: 4
    """

    type_: str = Field("LodgingReservation", const=True, alias="@type")
    lodgingUnitDescription: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A full description of the lodging unit.",
    )
    numChildren: "Optional[Union[List[Union[int, QuantitativeValue, str]], Union[int, QuantitativeValue, str]]]" = Field(
        None,
        description="The number of children staying in the unit.",
    )
    checkinTime: "Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]]" = Field(
        None,
        description="The earliest someone may check into a lodging establishment.",
    )
    numAdults: "Optional[Union[List[Union[int, QuantitativeValue, str]], Union[int, QuantitativeValue, str]]]" = Field(
        None,
        description="The number of adults staying in the unit.",
    )
    checkoutTime: "Optional[Union[List[Union[datetime, time, str]], Union[datetime, time, str]]]" = Field(
        None,
        description="The latest someone may check out of a lodging establishment.",
    )
    lodgingUnitType: "Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]]" = Field(
        None,
        description="Textual description of the unit type (including suite vs. room, size of bed, etc.).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    from datetime import time, datetime

    from pydantic_schemaorg.QualitativeValue import QualitativeValue

    LodgingReservation.update_forward_refs()
