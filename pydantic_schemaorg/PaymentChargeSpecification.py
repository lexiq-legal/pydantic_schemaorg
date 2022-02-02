from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    See: https://schema.org/PaymentChargeSpecification
    Model depth: 5
    """
    type_: str = Field("PaymentChargeSpecification", alias='@type')
    appliesToDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    appliesToPaymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        None,
        description="The payment method(s) to which the payment charge specification applies.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
