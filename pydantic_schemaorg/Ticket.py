from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Ticket(Intangible):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    See: https://schema.org/Ticket
    Model depth: 3
    """
    type_: str = Field("Ticket", alias='@type')
    underName: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The person or organization the reservation or ticket is for.",
    )
    ticketNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The unique identifier for the ticket.",
    )
    ticketToken: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.",
    )
    priceCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    totalPrice: Optional[Union[List[Union[Decimal, 'Number', str, 'Text', 'PriceSpecification']], Decimal, 'Number', str, 'Text', 'PriceSpecification']] = Field(
        None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping,"
     "etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",
    )
    dateIssued: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date the ticket was issued.",
    )
    ticketedSeat: Optional[Union[List[Union['Seat', str]], 'Seat', str]] = Field(
        None,
        description="The seat associated with the ticket.",
    )
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The organization issuing the ticket or permit.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Seat import Seat
