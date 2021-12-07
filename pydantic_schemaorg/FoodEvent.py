from pydantic import Field
from pydantic_schemaorg.Event import Event


class FoodEvent(Event):
    """Event type: Food event.

    See https://schema.org/FoodEvent.

    """
    type_: str = Field("FoodEvent", const=True, alias='@type')
    

FoodEvent.update_forward_refs()
