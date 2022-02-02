from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class FlightReservation(Reservation):
    """A reservation for air travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/FlightReservation
    Model depth: 4
    """
    type_: str = Field("FlightReservation", alias='@type')
    passengerSequenceNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The passenger's sequence number as assigned by the airline.",
    )
    securityScreening: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The type of security screening the passenger is subject to.",
    )
    passengerPriorityStatus: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        None,
        description="The priority status assigned to a passenger for security or boarding (e.g. FastTrack"
     "or Priority).",
    )
    boardingGroup: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The airline-specific indicator of boarding order / preference.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
