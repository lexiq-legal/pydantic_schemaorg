from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class SaleEvent(Event):
    """Event type: Sales event.

    See: https://schema.org/SaleEvent
    Model depth: 3
    """
    type_: str = Field("SaleEvent", alias='@type')
    

