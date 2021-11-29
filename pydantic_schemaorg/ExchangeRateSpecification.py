from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification
from pydantic_schemaorg.StructuredValue import StructuredValue


class ExchangeRateSpecification(StructuredValue):
    """A structured value representing exchange rate.

    See https://schema.org/ExchangeRateSpecification.

    """

    exchangeRateSpread: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The difference between the price at which a broker or other intermediary buys and sells"
     "foreign currency.",
    )
    currentExchangeRate: Optional[Union[List[UnitPriceSpecification], UnitPriceSpecification]] = Field(
        None,
        description="The current price of a currency.",
    )
    currency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies"
     "e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    locals().update({"@type": Field("ExchangeRateSpecification", const=True)})


ExchangeRateSpecification.update_forward_refs()
