from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class PreOrderAction(TradeAction):
    """An agent orders a (not yet released) object/product/service to be delivered/sent.

    See: https://schema.org/PreOrderAction
    Model depth: 4
    """
    type_: str = Field("PreOrderAction", alias='@type')
    

