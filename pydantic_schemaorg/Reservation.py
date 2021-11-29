from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from datetime import datetime
from decimal import Decimal
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class Reservation(Intangible):
    """Describes a reservation for travel, dining or an event. Some reservations require tickets."
     "Note: This type is for information about actual reservations, e.g. in confirmation"
     "emails or HTML pages with individual confirmations of reservations. For offers of tickets,"
     "restaurant reservations, flights, or rental cars, use [[Offer]].

    See https://schema.org/Reservation.

    """

    reservationId: Optional[Union[List[str], str]] = Field(
        None,
        description="A unique identifier for the reservation.",
    )
    programMembershipUsed: Any = Field(
        None,
        description="Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the"
     "reservation.",
    )
    underName: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The person or organization the reservation or ticket is for.",
    )
    modifiedTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date and time the reservation was modified.",
    )
    priceCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    totalPrice: Union[List[Union[Decimal, str, Any]], Union[Decimal, str, Any]] = Field(
        None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping,"
     "etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",
    )
    bookingAgent: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.",
    )
    reservationStatus: Any = Field(
        None,
        description="The current status of the reservation.",
    )
    provider: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    bookingTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date and time the reservation was booked.",
    )
    reservationFor: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The thing -- flight, event, restaurant,etc. being reserved.",
    )
    broker: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    reservedTicket: Any = Field(
        None,
        description="A ticket associated with the reservation.",
    )
    locals().update({"@type": Field("Reservation", const=True)})


Reservation.update_forward_refs()
