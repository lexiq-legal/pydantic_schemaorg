from pydantic import Field
from pydantic_schema_org.DeliveryMethod import DeliveryMethod
from typing import Any, Optional, Union, List
from pydantic_schema_org.TradeAction import TradeAction


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent.

    See https://schema.org/OrderAction.

    """

    deliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    locals().update({"@type": Field("OrderAction", const=True)})


OrderAction.update_forward_refs()
