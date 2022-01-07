from pydantic import StrictBool, Field
from typing import List, Optional, Union
from pydantic_schemaorg.DefinedRegion import DefinedRegion
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from pydantic_schemaorg.DeliveryChargeSpecification import DeliveryChargeSpecification
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingRateSettings(StructuredValue):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is"
     "designed for publication on an URL that may be referenced via the [[shippingSettingsLink]]"
     "property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished"
     "and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    See https://schema.org/ShippingRateSettings.

    """
    type_: str = Field("ShippingRateSettings", const=True, alias='@type')
    shippingLabel: Optional[Union[List[str], str]] = Field(
        None,
        description="Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    shippingDestination: Optional[Union[List[Union[DefinedRegion, str]], Union[DefinedRegion, str]]] = Field(
        None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways e.g. postalCode ranges.",
    )
    shippingRate: Optional[Union[List[Union[MonetaryAmount, str]], Union[MonetaryAmount, str]]] = Field(
        None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
     "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    freeShippingThreshold: Optional[Union[List[Union[DeliveryChargeSpecification, MonetaryAmount, str]], Union[DeliveryChargeSpecification, MonetaryAmount, str]]] = Field(
        None,
        description="A monetary value above which (or equal to) the shipping rate becomes free. Intended to"
     "be used via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching"
     "this [[ShippingRateSettings]].",
    )
    isUnlabelledFallback: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]]"
     "or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]]"
     "published by the same merchant, when referenced by a [[shippingSettingsLink]] in those"
     "settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel"
     "(for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]),"
     "since this property is for use with unlabelled settings.",
    )
    

ShippingRateSettings.update_forward_refs()
