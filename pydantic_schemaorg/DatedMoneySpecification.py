from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.StructuredValue import StructuredValue


class DatedMoneySpecification(StructuredValue):
    """A DatedMoneySpecification represents monetary values with optional start and end"
     "dates. For example, this could represent an employee's salary over a specific period"
     "of time. __Note:__ This type has been superseded by [[MonetaryAmount]] use of that type"
     "is recommended

    See: https://schema.org/DatedMoneySpecification
    Model depth: 4
    """

    type_: str = Field("DatedMoneySpecification", const=True, alias="@type")
    amount: "Optional[Union[List[Union[Decimal, MonetaryAmount, str]], Union[Decimal, MonetaryAmount, str]]]" = Field(
        None,
        description="The amount of money.",
    )
    endDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    startDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    currency: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
        'currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. "USD"; [Ticker'
        "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies"
        'e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types e.g. "Ithaca HOUR".',
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount

    from datetime import date, datetime

    DatedMoneySpecification.update_forward_refs()
