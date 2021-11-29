from pydantic import Field, AnyUrl
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class UnitPriceSpecification(PriceSpecification):
    """The price asked for a given offer by the respective organization or person.

    See https://schema.org/UnitPriceSpecification.

    """

    billingStart: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Specifies after how much time this price (or price component) becomes valid and billing"
     "starts. Can be used, for example, to model a price increase after the first year of a subscription."
     "The unit of measurement is specified by the unitCode property.",
    )
    billingIncrement: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="This property specifies the minimal quantity and rounding increment that will be the"
     "basis for the billing. The unit of measurement is specified by the unitCode property.",
    )
    unitText: Optional[Union[List[str], str]] = Field(
        None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    priceType: Optional[Union[List[Union[str, PriceTypeEnumeration]], Union[str, PriceTypeEnumeration]]] = Field(
        None,
        description="Defines the type of a price specified for an offered product, for example a list price,"
     "a (temporary) sale price or a manufacturer suggested retail price. If multiple prices"
     "are specified for an offer the [[priceType]] property can be used to identify the type"
     "of each such specified price. The value of priceType can be specified as a value from enumeration"
     "PriceTypeEnumeration or as a free form text string for price types that are not already"
     "predefined in PriceTypeEnumeration.",
    )
    billingDuration: Union[List[Union[Decimal, QuantitativeValue, Any]], Union[Decimal, QuantitativeValue, Any]] = Field(
        None,
        description="Specifies for how long this price (or price component) will be billed. Can be used, for"
     "example, to model the contractual duration of a subscription or payment plan. Type can"
     "be either a Duration or a Number (in which case the unit of measurement, for example month,"
     "is specified by the unitCode property).",
    )
    referenceQuantity: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity."
     "This property is a replacement for unitOfMeasurement for the advanced cases where the"
     "price does not relate to a standard unit.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    priceComponentType: Optional[Union[List[PriceComponentTypeEnumeration], PriceComponentTypeEnumeration]] = Field(
        None,
        description="Identifies a price component (for example, a line item on an invoice), part of the total"
     "price for an offer.",
    )
    locals().update({"@type": Field("UnitPriceSpecification", const=True)})


UnitPriceSpecification.update_forward_refs()
