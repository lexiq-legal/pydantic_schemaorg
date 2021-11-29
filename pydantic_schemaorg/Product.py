from pydantic import Field, AnyUrl
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from typing import Any, Union, List, Optional
from datetime import date
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Review import Review


class Product(Thing):
    """Any offered product or service. For example: a pair of shoes; a concert ticket; the rental"
     "of a car; a haircut; or an episode of a TV show streamed online.

    See https://schema.org/Product.

    """

    pattern: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    hasMeasurement: Any = Field(
        None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    offers: Any = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    color: Optional[Union[List[str], str]] = Field(
        None,
        description="The color of the product.",
    )
    isAccessoryOrSparePartFor: Any = Field(
        None,
        description="A pointer to another product (or multiple products) for which this product is an accessory"
     "or spare part.",
    )
    productID: Optional[Union[List[str], str]] = Field(
        None,
        description="The product identifier, such as ISBN. For example: ``` meta itemprop=\"productID\""
     "content=\"isbn:123-456-789\" ```.",
    )
    model: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The model of the product. Use with the URL of a ProductModel or a textual representation"
     "of the model identifier. The URL of the ProductModel can be from an external source. It"
     "is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14"
     "and mpn properties.",
    )
    depth: Any = Field(
        None,
        description="The depth of the item.",
    )
    weight: Any = Field(
        None,
        description="The weight of the product or person.",
    )
    gtin13: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    productionDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date of production of the item, e.g. vehicle.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[str], str]] = Field(
        None,
        description="An award won by or for this item.",
    )
    gtin8: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    nsn: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)"
     "(nsn) of a [[Product]].",
    )
    countryOfOrigin: Any = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    manufacturer: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The manufacturer of the product.",
    )
    brand: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    hasMerchantReturnPolicy: Any = Field(
        None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    hasEnergyConsumptionDetails: Any = Field(
        None,
        description="Defines the energy efficiency Category (also known as \"class\" or \"rating\") for"
     "a product according to an international energy efficiency standard.",
    )
    slogan: Optional[Union[List[str], str]] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    isSimilarTo: Any = Field(
        None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    height: Any = Field(
        None,
        description="The height of the item.",
    )
    size: Union[List[Union[str, DefinedTerm, Any]], Union[str, DefinedTerm, Any]] = Field(
        None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    releaseDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The release date of a product or product model. This can be used to distinguish the exact"
     "variant of a product.",
    )
    logo: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="An associated logo.",
    )
    mpn: Optional[Union[List[str], str]] = Field(
        None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",
    )
    countryOfLastProcessing: Optional[Union[List[str], str]] = Field(
        None,
        description="The place where the item (typically [[Product]]) was last processed and tested before"
     "importation.",
    )
    awards: Optional[Union[List[str], str]] = Field(
        None,
        description="Awards won by or for this item.",
    )
    gtin12: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    width: Any = Field(
        None,
        description="The width of the item.",
    )
    audience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    gtin14: Optional[Union[List[str], str]] = Field(
        None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    material: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    isRelatedTo: Any = Field(
        None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    inProductGroupWithID: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].",
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
    isConsumableFor: Any = Field(
        None,
        description="A pointer to another product (or multiple products) for which this product is a consumable.",
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
    itemCondition: Any = Field(
        None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    additionalProperty: Any = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    isVariantOf: Any = Field(
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
    countryOfAssembly: Optional[Union[List[str], str]] = Field(
        None,
        description="The place where the product was assembled.",
    )
    purchaseDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date the item e.g. vehicle was purchased by the current owner.",
    )
    locals().update({"@type": Field("Product", const=True)})


Product.update_forward_refs()
