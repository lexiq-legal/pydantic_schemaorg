from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.QuantitativeValueDistribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """A statistical distribution of monetary amounts.

    See https://schema.org/MonetaryAmountDistribution.

    """

    currency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies"
     "e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    locals().update({"@type": Field("MonetaryAmountDistribution", const=True)})


MonetaryAmountDistribution.update_forward_refs()
