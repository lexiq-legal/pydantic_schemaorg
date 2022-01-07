from pydantic import Field
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from typing import List, Optional, Union
from pydantic_schemaorg.TradeAction import TradeAction


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent.

    See https://schema.org/OrderAction.

    """
    type_: str = Field("OrderAction", const=True, alias='@type')
    deliveryMethod: Optional[Union[List[Union[DeliveryMethod, str]], Union[DeliveryMethod, str]]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    

OrderAction.update_forward_refs()
