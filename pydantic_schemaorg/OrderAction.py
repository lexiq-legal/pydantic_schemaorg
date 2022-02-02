from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class OrderAction(TradeAction):
    """An agent orders an object/product/service to be delivered/sent.

    See: https://schema.org/OrderAction
    Model depth: 4
    """
    type_: str = Field("OrderAction", alias='@type')
    deliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
