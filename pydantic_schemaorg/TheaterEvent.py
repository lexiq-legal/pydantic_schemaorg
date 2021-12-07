from pydantic import Field
from pydantic_schemaorg.Event import Event


class TheaterEvent(Event):
    """Event type: Theater performance.

    See https://schema.org/TheaterEvent.

    """
    type_: str = Field("TheaterEvent", const=True, alias='@type')
    

TheaterEvent.update_forward_refs()
