from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class FoodEvent(Event):
    """Event type: Food event.

    See: https://schema.org/FoodEvent
    Model depth: 3
    """
    type_: str = Field("FoodEvent", alias='@type')
    

