from pydantic import Field, AnyUrl
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from datetime import date, datetime, time
from pydantic_schemaorg.BusinessEntityType import BusinessEntityType
from pydantic_schemaorg.ItemAvailability import ItemAvailability
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
from decimal import Decimal
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition
from pydantic_schemaorg.Intangible import Intangible


class Offer(Intangible):
    """An offer to transfer some rights to an item or to provide a service — for example, an offer"
     "to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet,"
     "to repair a motorcycle, or to loan a book. Note: As the [[businessFunction]] property,"
     "which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to"
     "http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction"
     "value can be assumed to be an offer to sell. For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related"
     "fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator)"
     "and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide)"
     "from [GS1](http://www.gs1.org/).

    See https://schema.org/Offer.

    """

    hasMeasurement: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    includesObject: Any = Field(
        None,
        description="This links to a node or nodes indicating the exact quantity of the products included in"
     "an [[Offer]] or [[ProductCollection]].",
    )
    areaServed: Union[List[Union[str, Place, AdministrativeArea, Any]], Union[str, Place, AdministrativeArea, Any]] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    availableDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="The delivery method(s) available for this offer.",
    )
    serialNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The serial number or any alphanumeric identifier of a particular product. When attached"
     "to an offer, it is a shortcut for the serial number of the product included in the offer.",
    )
    gtin13: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    priceValidUntil: Optional[Union[List[date], date]] = Field(
        None,
        description="The date after which the price is no longer available.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    eligibleCustomerType: Optional[Union[List[BusinessEntityType], BusinessEntityType]] = Field(
        None,
        description="The type(s) of customers for which the given offer is valid.",
    )
    availability: Optional[Union[List[ItemAvailability], ItemAvailability]] = Field(
        None,
        description="The availability of this item&#x2014;for example In stock, Out of stock, Pre-order,"
     "etc.",
    )
    gtin8: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    leaseLength: Union[List[Union[QuantitativeValue, Any]], Union[QuantitativeValue, Any]] = Field(
        None,
        description="Length of the lease for some [[Accommodation]], either particular to some [[Offer]]"
     "or in some cases intrinsic to the property.",
    )
    eligibleTransactionVolume: Optional[Union[List[PriceSpecification], PriceSpecification]] = Field(
        None,
        description="The transaction volume, in a monetary unit, for which the offer or price specification"
     "is valid, e.g. for indicating a minimal purchasing volume, to express free shipping"
     "above a certain order volume, or to limit the acceptance of credit cards to purchases"
     "to a certain minimal amount.",
    )
    acceptedPaymentMethod: Union[List[Union[PaymentMethod, Any]], Union[PaymentMethod, Any]] = Field(
        None,
        description="The payment method(s) accepted by seller for this offer.",
    )
    businessFunction: Any = Field(
        None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component"
     "of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    eligibleDuration: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The duration for which the given offer is valid.",
    )
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[MerchantReturnPolicy], MerchantReturnPolicy]] = Field(
        None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    availabilityStarts: Optional[Union[List[Union[datetime, time, date]], Union[datetime, time, date]]] = Field(
        None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    priceCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217)"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies e.g. \"BTC\"; well known names for [Local Exchange Tradings Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types e.g. \"Ithaca HOUR\".",
    )
    price: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
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
    eligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    seller: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    warranty: Any = Field(
        None,
        description="The warranty promise(s) included in the offer.",
    )
    deliveryLeadTime: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse"
     "or being prepared for pickup, in case the delivery method is on site pickup.",
    )
    mpn: Optional[Union[List[str], str]] = Field(
        None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",
    )
    gtin12: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    availableAtOrFrom: Optional[Union[List[Place], Place]] = Field(
        None,
        description="The place(s) from which the offer can be obtained (e.g. store locations).",
    )
    offeredBy: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A pointer to the organization or person making the offer.",
    )
    validFrom: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date when the item becomes valid.",
    )
    itemOffered: Union[List[Union[Product, CreativeWork, Service, Event, Any]], Union[Product, CreativeWork, Service, Event, Any]] = Field(
        None,
        description="An item being offered (or demanded). The transactional nature of the offer or demand"
     "is documented using [[businessFunction]], e.g. sell, lease etc. While several common"
     "expected types are listed explicitly in this definition, others can be used. Using a"
     "second type, such as Product or a subtype of Product, can clarify the nature of the offer.",
    )
    gtin14: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    availabilityEnds: Optional[Union[List[Union[datetime, time, date]], Union[datetime, time, date]]] = Field(
        None,
        description="The end of the availability of the product or service included in the offer.",
    )
    validThrough: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    addOn: Any = Field(
        None,
        description="An additional offer that can only be obtained in combination with the first base offer"
     "(e.g. supplements and extensions that are available for a surcharge).",
    )
    reviews: Optional[Union[List[Review], Review]] = Field(
        None,
        description="Review of the item.",
    )
    sku: Optional[Union[List[str], str]] = Field(
        None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service,"
     "or the product to which the offer refers.",
    )
    gtin: Optional[Union[List[str], str]] = Field(
        None,
        description="A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin))."
     "GTINs identify trade items, including products and services, using numeric identification"
     "codes. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]],"
     "and [[gtin14]] properties. The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/)"
     "express GTINs as URLs. A correct [[gtin]] value should be a valid GTIN, which means that"
     "it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a \"GS1 Digital Link\""
     "URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)"
     "and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for"
     "more details. Left-padding of the gtin values is not required or encouraged.",
    )
    review: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A review of the item.",
    )
    itemCondition: Optional[Union[List[OfferItemCondition], OfferItemCondition]] = Field(
        None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    inventoryLevel: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The current approximate inventory level for the item or items.",
    )
    advanceBookingRequirement: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The amount of time that is required between accepting the offer and the actual usage of"
     "the resource or service.",
    )
    priceSpecification: Optional[Union[List[PriceSpecification], PriceSpecification]] = Field(
        None,
        description="One or more detailed price specifications, indicating the unit price and delivery or"
     "payment charges.",
    )
    ineligibleRegion: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    eligibleQuantity: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The interval and unit of measurement of ordering quantities for which the offer or price"
     "specification is valid. This allows e.g. specifying that a certain freight charge is"
     "valid only for a certain quantity.",
    )
    shippingDetails: Any = Field(
        None,
        description="Indicates information about the shipping policies and options associated with an [[Offer]].",
    )
    locals().update({"@type": Field("Offer", const=True)})


Offer.update_forward_refs()
