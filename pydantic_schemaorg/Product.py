from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Product(Thing):
    """Any offered product or service. For example: a pair of shoes; a concert ticket; the rental"
     "of a car; a haircut; or an episode of a TV show streamed online.

    See: https://schema.org/Product
    Model depth: 2
    """
    type_: str = Field("Product", alias='@type')
    pattern: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    hasMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    offers: Optional[Union[List[Union['Demand', 'Offer', str]], 'Demand', 'Offer', str]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    color: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The color of the product.",
    )
    isAccessoryOrSparePartFor: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        None,
        description="A pointer to another product (or multiple products) for which this product is an accessory"
     "or spare part.",
    )
    productID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The product identifier, such as ISBN. For example: ``` meta itemprop=\"productID\""
     "content=\"isbn:123-456-789\" ```.",
    )
    model: Optional[Union[List[Union[str, 'Text', 'ProductModel']], str, 'Text', 'ProductModel']] = Field(
        None,
        description="The model of the product. Use with the URL of a ProductModel or a textual representation"
     "of the model identifier. The URL of the ProductModel can be from an external source. It"
     "is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14"
     "and mpn properties.",
    )
    depth: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        None,
        description="The depth of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The weight of the product or person.",
    )
    gtin13: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    productionDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date of production of the item, e.g. vehicle.",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An award won by or for this item.",
    )
    gtin8: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    nsn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)"
     "(nsn) of a [[Product]].",
    )
    countryOfOrigin: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    manufacturer: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The manufacturer of the product.",
    )
    brand: Optional[Union[List[Union['Organization', 'Brand', str]], 'Organization', 'Brand', str]] = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory']] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[Union['MerchantReturnPolicy', str]], 'MerchantReturnPolicy', str]] = Field(
        None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    hasEnergyConsumptionDetails: Optional[Union[List[Union['EnergyConsumptionDetails', str]], 'EnergyConsumptionDetails', str]] = Field(
        None,
        description="Defines the energy efficiency Category (also known as \"class\" or \"rating\") for"
     "a product according to an international energy efficiency standard.",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    isSimilarTo: Optional[Union[List[Union['Service', 'Product', str]], 'Service', 'Product', str]] = Field(
        None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    height: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        None,
        description="The height of the item.",
    )
    size: Optional[Union[List[Union[str, 'Text', 'SizeSpecification', 'QuantitativeValue', 'DefinedTerm']], str, 'Text', 'SizeSpecification', 'QuantitativeValue', 'DefinedTerm']] = Field(
        None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    releaseDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The release date of a product or product model. This can be used to distinguish the exact"
     "variant of a product.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        None,
        description="An associated logo.",
    )
    mpn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",
    )
    countryOfLastProcessing: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The place where the item (typically [[Product]]) was last processed and tested before"
     "importation.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Awards won by or for this item.",
    )
    gtin12: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    width: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        None,
        description="The width of the item.",
    )
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    gtin14: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    material: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Product']], AnyUrl, 'URL', str, 'Text', 'Product']] = Field(
        None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    isRelatedTo: Optional[Union[List[Union['Service', 'Product', str]], 'Service', 'Product', str]] = Field(
        None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    inProductGroupWithID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].",
    )
    reviews: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="Review of the item.",
    )
    sku: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service,"
     "or the product to which the offer refers.",
    )
    isConsumableFor: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        None,
        description="A pointer to another product (or multiple products) for which this product is a consumable.",
    )
    gtin: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
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
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="A review of the item.",
    )
    itemCondition: Optional[Union[List[Union['OfferItemCondition', str]], 'OfferItemCondition', str]] = Field(
        None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    additionalProperty: Optional[Union[List[Union['PropertyValue', str]], 'PropertyValue', str]] = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    isVariantOf: Optional[Union[List[Union['ProductModel', 'ProductGroup', str]], 'ProductModel', 'ProductGroup', str]] = Field(
        None,
        description="Indicates the kind of product that this is a variant of. In the case of [[ProductModel]],"
     "this is a pointer (from a ProductModel) to a base product from which this product is a variant."
     "It is safe to infer that the variant inherits all product features from the base model,"
     "unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the"
     "group description also serves as a template, representing a set of Products that vary"
     "on explicitly defined, specific dimensions only (so it defines both a set of variants,"
     "as well as which values distinguish amongst those variants). When used with [[ProductGroup]],"
     "this property can apply to any [[Product]] included in the group.",
    )
    countryOfAssembly: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The place where the product was assembled.",
    )
    purchaseDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date the item e.g. vehicle was purchased by the current owner.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.ProductModel import ProductModel
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic_schemaorg.EnergyConsumptionDetails import EnergyConsumptionDetails
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.SizeSpecification import SizeSpecification
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.OfferItemCondition import OfferItemCondition
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.ProductGroup import ProductGroup
