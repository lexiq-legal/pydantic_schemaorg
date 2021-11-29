from pydantic import Field
from pydantic_schema_org.DeliveryMethod import DeliveryMethod
from typing import Any, Optional, Union, List
from pydantic_schema_org.PaymentMethod import PaymentMethod
from pydantic_schema_org.PriceSpecification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    See https://schema.org/PaymentChargeSpecification.

    """

    appliesToDeliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    appliesToPaymentMethod: Optional[Union[List[PaymentMethod], PaymentMethod]] = Field(
        None,
        description="The payment method(s) to which the payment charge specification applies.",
    )
    locals().update({"@type": Field("PaymentChargeSpecification", const=True)})


PaymentChargeSpecification.update_forward_refs()
