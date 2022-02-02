from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl, StrictBool


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OfferShippingDetails(StructuredValue):
    """OfferShippingDetails represents information about shipping destinations. Multiple"
     "of these entities can be used to represent different shipping rates for different destinations:"
     "One entity for Alaska/Hawaii. A different one for continental US.A different one for"
     "all France. Multiple of these entities can be used to represent different shipping costs"
     "and delivery times. Two entities that are identical but differ in rate and time: e.g."
     "Cheaper and slower: $5 in 5-7days or Fast and expensive: $15 in 1-2 days.

    See: https://schema.org/OfferShippingDetails
    Model depth: 4
    """
    type_: str = Field("OfferShippingDetails", alias='@type')
    shippingLabel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    shippingDestination: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways e.g. postalCode ranges.",
    )
    shippingRate: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
     "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    shippingSettingsLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]]"
     "details.",
    )
    deliveryTime: Optional[Union[List[Union['ShippingDeliveryTime', str]], 'ShippingDeliveryTime', str]] = Field(
        None,
        description="The total delay between the receipt of the order and the goods reaching the final customer.",
    )
    transitTimeLabel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
