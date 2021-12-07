from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from typing import Any, Optional, Union, List
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    See https://schema.org/PaymentChargeSpecification.

    """
    type_: str = Field("PaymentChargeSpecification", const=True, alias='@type')
    appliesToDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    appliesToPaymentMethod: Optional[Union[List[PaymentMethod], PaymentMethod]] = Field(
        None,
        description="The payment method(s) to which the payment charge specification applies.",
    )
    

PaymentChargeSpecification.update_forward_refs()
