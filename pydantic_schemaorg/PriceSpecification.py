from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool
from typing import Union, Optional, List
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class PriceSpecification(StructuredValue):
    """A structured value representing a price or price range. Typically, only the subclasses"
     "of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe"
     "independent amounts of money such as a salary, credit card limits, etc.

    See: https://schema.org/PriceSpecification
    Model depth: 4
    """
    type_: str = Field("PriceSpecification", alias='@type')
    valueAddedTaxIncluded: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Specifies whether the applicable value-added tax (VAT) is included in the price specification"
     "or not.",
    )
    eligibleTransactionVolume: Optional[Union[List[Union['PriceSpecification', str]], 'PriceSpecification', str]] = Field(
        None,
        description="The transaction volume, in a monetary unit, for which the offer or price specification"
     "is valid, e.g. for indicating a minimal purchasing volume, to express free shipping"
     "above a certain order volume, or to limit the acceptance of credit cards to purchases"
     "to a certain minimal amount.",
    )
    priceCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    price: Optional[Union[List[Union[Decimal, 'Number', str, 'Text']], Decimal, 'Number', str, 'Text']] = Field(
        None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification"
     "and its subtypes. Usage guidelines: * Use the [[priceCurrency]] property (with standard"
     "formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217) e.g."
     "\"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\") instead of including [ambiguous"
     "symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)"
     "such as '$' in the value. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
     "a decimal point. Avoid using these symbols as a readability separator. * Note that both"
     "[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)"
     "and Microdata syntax allow the use of a \"content=\" attribute for publishing simple"
     "machine-readable values alongside more human-friendly formatting. * Use values from"
     "0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
     "similiar Unicode symbols.",
    )
    maxPrice: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The highest price if the price is a range.",
    )
    minPrice: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The lowest price if the price is a range.",
    )
    validFrom: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    eligibleQuantity: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The interval and unit of measurement of ordering quantities for which the offer or price"
     "specification is valid. This allows e.g. specifying that a certain freight charge is"
     "valid only for a certain quantity.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
