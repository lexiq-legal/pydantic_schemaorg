from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    See: https://schema.org/PaymentChargeSpecification
    Model depth: 5
    """
    type_: str = Field(default="PaymentChargeSpecification", alias='@type', const=True)
    appliesToDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    appliesToPaymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        default=None,
        description="The payment method(s) to which the payment charge specification applies.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
