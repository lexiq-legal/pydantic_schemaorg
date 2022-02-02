from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class DatedMoneySpecification(StructuredValue):
    """A DatedMoneySpecification represents monetary values with optional start and end"
     "dates. For example, this could represent an employee's salary over a specific period"
     "of time. __Note:__ This type has been superseded by [[MonetaryAmount]] use of that type"
     "is recommended

    See: https://schema.org/DatedMoneySpecification
    Model depth: 4
    """
    type_: str = Field("DatedMoneySpecification", alias='@type')
    amount: Optional[Union[List[Union[Decimal, 'Number', 'MonetaryAmount', str]], Decimal, 'Number', 'MonetaryAmount', str]] = Field(
        None,
        description="The amount of money.",
    )
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    currency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies"
     "e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
