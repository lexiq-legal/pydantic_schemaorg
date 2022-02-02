from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ExchangeRateSpecification(StructuredValue):
    """A structured value representing exchange rate.

    See: https://schema.org/ExchangeRateSpecification
    Model depth: 4
    """
    type_: str = Field("ExchangeRateSpecification", alias='@type')
    exchangeRateSpread: Optional[Union[List[Union[Decimal, 'Number', 'MonetaryAmount', str]], Decimal, 'Number', 'MonetaryAmount', str]] = Field(
        None,
        description="The difference between the price at which a broker or other intermediary buys and sells"
     "foreign currency.",
    )
    currentExchangeRate: Optional[Union[List[Union['UnitPriceSpecification', str]], 'UnitPriceSpecification', str]] = Field(
        None,
        description="The current price of a currency.",
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
    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification
    from pydantic_schemaorg.Text import Text
