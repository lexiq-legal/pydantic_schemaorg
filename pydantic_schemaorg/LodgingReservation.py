from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from datetime import datetime, time
from pydantic_schemaorg.QualitativeValue import QualitativeValue
from pydantic_schemaorg.Reservation import Reservation


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See https://schema.org/LodgingReservation.

    """

    lodgingUnitDescription: Optional[Union[List[str], str]] = Field(
        None,
        description="A full description of the lodging unit.",
    )
    numChildren: Optional[Union[List[Union[int, QuantitativeValue]], Union[int, QuantitativeValue]]] = Field(
        None,
        description="The number of children staying in the unit.",
    )
    checkinTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The earliest someone may check into a lodging establishment.",
    )
    numAdults: Optional[Union[List[Union[int, QuantitativeValue]], Union[int, QuantitativeValue]]] = Field(
        None,
        description="The number of adults staying in the unit.",
    )
    checkoutTime: Optional[Union[List[Union[datetime, time]], Union[datetime, time]]] = Field(
        None,
        description="The latest someone may check out of a lodging establishment.",
    )
    lodgingUnitType: Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]] = Field(
        None,
        description="Textual description of the unit type (including suite vs. room, size of bed, etc.).",
    )
    locals().update({"@type": Field("LodgingReservation", const=True)})


LodgingReservation.update_forward_refs()
