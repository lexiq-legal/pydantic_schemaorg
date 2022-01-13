from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Action import Action


class TradeAction(Action):
    """The act of participating in an exchange of goods and services for monetary compensation."
     "An agent trades an object, product or service with a participant in exchange for a one"
     "time or periodic payment.

    See: https://schema.org/TradeAction
    Model depth: 3
    """

    type_: str = Field("TradeAction", const=True, alias="@type")
    priceCurrency: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
        "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
        'e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)'
        'for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types e.g. "Ithaca HOUR".',
    )
    price: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification"
        "and its subtypes. Usage guidelines: * Use the [[priceCurrency]] property (with standard"
        "formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g."
        '"USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)'
        'for cryptocurrencies e.g. "BTC"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types e.g. "Ithaca HOUR") instead of including [ambiguous'
        "symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)"
        "such as '$' in the value. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
        "a decimal point. Avoid using these symbols as a readability separator. * Note that both"
        "[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)"
        'and Microdata syntax allow the use of a "content=" attribute for publishing simple'
        "machine-readable values alongside more human-friendly formatting. * Use values from"
        "0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
        "similiar Unicode symbols.",
    )
    priceSpecification: "Optional[Union[List[Union[PriceSpecification, str]], Union[PriceSpecification, str]]]" = Field(
        None,
        description="One or more detailed price specifications, indicating the unit price and delivery or"
        "payment charges.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.PriceSpecification import PriceSpecification

    TradeAction.update_forward_refs()
