from pydantic import Field, StrictBool
from pydantic_schemaorg.DefinedRegion import DefinedRegion
from typing import Any, Union, List, Optional
from pydantic_schemaorg.StructuredValue import StructuredValue


class DeliveryTimeSettings(StructuredValue):
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating"
     "to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]]"
     "property of a [[OfferShippingDetails]]. Several occurrences can be published, distinguished"
     "(and identified/referenced) by their different values for [[transitTimeLabel]].

    See https://schema.org/DeliveryTimeSettings.

    """

    shippingDestination: Optional[Union[List[DefinedRegion], DefinedRegion]] = Field(
        None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways e.g. postalCode ranges.",
    )
    isUnlabelledFallback: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]]"
     "or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]]"
     "published by the same merchant, when referenced by a [[shippingSettingsLink]] in those"
     "settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel"
     "(for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]),"
     "since this property is for use with unlabelled settings.",
    )
    deliveryTime: Any = Field(
        None,
        description="The total delay between the receipt of the order and the goods reaching the final customer.",
    )
    transitTimeLabel: Optional[Union[List[str], str]] = Field(
        None,
        description="Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    locals().update({"@type": Field("DeliveryTimeSettings", const=True)})


DeliveryTimeSettings.update_forward_refs()
