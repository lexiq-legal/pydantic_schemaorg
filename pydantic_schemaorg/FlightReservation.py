from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.QualitativeValue import QualitativeValue
from pydantic_schemaorg.Reservation import Reservation


class FlightReservation(Reservation):
    """A reservation for air travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See https://schema.org/FlightReservation.

    """
    type_: str = Field("FlightReservation", const=True, alias='@type')
    passengerSequenceNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The passenger's sequence number as assigned by the airline.",
    )
    securityScreening: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of security screening the passenger is subject to.",
    )
    passengerPriorityStatus: Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]] = Field(
        None,
        description="The priority status assigned to a passenger for security or boarding (e.g. FastTrack"
     "or Priority).",
    )
    boardingGroup: Optional[Union[List[str], str]] = Field(
        None,
        description="The airline-specific indicator of boarding order / preference.",
    )
    

FlightReservation.update_forward_refs()
