from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import Any, Union, List, Optional
from datetime import time
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingDeliveryTime(StructuredValue):
    """ShippingDeliveryTime provides various pieces of information about delivery times"
     "for shipping.

    See https://schema.org/ShippingDeliveryTime.

    """

    transitTime: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The typical delay the order has been sent for delivery and the goods reach the final customer."
     "Typical properties: minValue, maxValue, unitCode (d for DAY).",
    )
    cutoffTime: Optional[Union[List[time], time]] = Field(
        None,
        description="Order cutoff time allows merchants to describe the time after which they will no longer"
     "process orders received on that day. For orders processed after cutoff time, one day"
     "gets added to the delivery time estimate. This property is expected to be most typically"
     "used via the [[ShippingRateSettings]] publication pattern. The time is indicated"
     "using the ISO-8601 Time format, e.g. \"23:30:00-05:00\" would represent 6:30 pm Eastern"
     "Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).",
    )
    handlingTime: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse"
     "or being prepared for pickup, in case the delivery method is on site pickup. Typical properties:"
     "minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean"
     "business days (if a unitCode is used, coded as \"d\"), i.e. only counting days when the"
     "business normally operates.",
    )
    businessDays: Any = Field(
        None,
        description="Days of the week when the merchant typically operates, indicated via opening hours markup.",
    )
    locals().update({"@type": Field("ShippingDeliveryTime", const=True)})


ShippingDeliveryTime.update_forward_refs()
