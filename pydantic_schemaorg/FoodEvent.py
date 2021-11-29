from pydantic import Field
from pydantic_schemaorg.Event import Event


class FoodEvent(Event):
    """Event type: Food event.

    See https://schema.org/FoodEvent.

    """

    locals().update({"@type": Field("FoodEvent", const=True)})


FoodEvent.update_forward_refs()
