from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class DeliveryTimeSettings(StructuredValue):
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating"
     "to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]]"
     "property of a [[OfferShippingDetails]]. Several occurrences can be published, distinguished"
     "(and identified/referenced) by their different values for [[transitTimeLabel]].

    See: https://schema.org/DeliveryTimeSettings
    Model depth: 4
    """
    type_: str = Field("DeliveryTimeSettings", alias='@type')
    shippingDestination: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways e.g. postalCode ranges.",
    )
    isUnlabelledFallback: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]]"
     "or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]]"
     "published by the same merchant, when referenced by a [[shippingSettingsLink]] in those"
     "settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel"
     "(for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]),"
     "since this property is for use with unlabelled settings.",
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
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
    from pydantic_schemaorg.Text import Text
