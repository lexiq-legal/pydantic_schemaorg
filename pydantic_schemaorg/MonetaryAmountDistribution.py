from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.QuantitativeValueDistribution import QuantitativeValueDistribution


class MonetaryAmountDistribution(QuantitativeValueDistribution):
    """A statistical distribution of monetary amounts.

    See: https://schema.org/MonetaryAmountDistribution
    Model depth: 5
    """
    type_: str = Field("MonetaryAmountDistribution", alias='@type')
    currency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies"
     "e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
