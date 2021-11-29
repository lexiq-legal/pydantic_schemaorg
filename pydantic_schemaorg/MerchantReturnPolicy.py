from pydantic import Field, AnyUrl, StrictBool
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration
from datetime import date, datetime
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition
from decimal import Decimal
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicy(Intangible):
    """A MerchantReturnPolicy provides information about product return policies associated"
     "with an [[Organization]], [[Product]], or [[Offer]].

    See https://schema.org/MerchantReturnPolicy.

    """

    customerRemorseReturnFees: Optional[Union[List[ReturnFeesEnumeration], ReturnFeesEnumeration]] = Field(
        None,
        description="The type of return fees if the product is returned due to customer remorse.",
    )
    customerRemorseReturnShippingFeesAmount: Any = Field(
        None,
        description="The amount of shipping costs if a product is returned due to customer remorse. Applicable"
     "when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].",
    )
    inStoreReturnsOffered: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Are in-store returns offered? (for more advanced return methods use the [[returnMethod]]"
     "property)",
    )
    itemDefectReturnShippingFeesAmount: Any = Field(
        None,
        description="Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]]"
     "equals [[ReturnShippingFees]].",
    )
    returnFees: Optional[Union[List[ReturnFeesEnumeration], ReturnFeesEnumeration]] = Field(
        None,
        description="The type of return fees for purchased products (for any return reason)",
    )
    merchantReturnLink: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="Specifies a Web page or service by URL, for product returns.",
    )
    itemDefectReturnLabelSource: Optional[Union[List[ReturnLabelSourceEnumeration], ReturnLabelSourceEnumeration]] = Field(
        None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a defect product.",
    )
    merchantReturnDays: Optional[Union[List[Union[datetime, int, date]], Union[datetime, int, date]]] = Field(
        None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",
    )
    returnLabelSource: Optional[Union[List[ReturnLabelSourceEnumeration], ReturnLabelSourceEnumeration]] = Field(
        None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned for any reason.",
    )
    returnPolicySeasonalOverride: Any = Field(
        None,
        description="Seasonal override of a return policy.",
    )
    refundType: Any = Field(
        None,
        description="A refund type, from an enumerated list.",
    )
    returnPolicyCategory: Any = Field(
        None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    returnPolicyCountry: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The country where the product has to be sent to for returns, for example \"Ireland\" using"
     "the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1"
     "alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this"
     "can be different from the country where the product was originally shipped from or sent"
     "too.",
    )
    itemDefectReturnFees: Optional[Union[List[ReturnFeesEnumeration], ReturnFeesEnumeration]] = Field(
        None,
        description="The type of return fees for returns of defect products.",
    )
    returnMethod: Optional[Union[List[ReturnMethodEnumeration], ReturnMethodEnumeration]] = Field(
        None,
        description="The type of return method offered, specified from an enumeration.",
    )
    itemCondition: Optional[Union[List[OfferItemCondition], OfferItemCondition]] = Field(
        None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    restockingFee: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use"
     "[[Number]] to specify a percentage of the product price paid by the customer.",
    )
    additionalProperty: Optional[Union[List[PropertyValue], PropertyValue]] = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    returnShippingFeesAmount: Any = Field(
        None,
        description="Amount of shipping costs for product returns (for any reason). Applicable when property"
     "[[returnFees]] equals [[ReturnShippingFees]].",
    )
    customerRemorseReturnLabelSource: Optional[Union[List[ReturnLabelSourceEnumeration], ReturnLabelSourceEnumeration]] = Field(
        None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned due to customer remorse.",
    )
    locals().update({"@type": Field("MerchantReturnPolicy", const=True)})


MerchantReturnPolicy.update_forward_refs()
