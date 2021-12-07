from pydantic import Field
from pydantic_schemaorg.Event import Event


class DanceEvent(Event):
    """Event type: A social dance.

    See https://schema.org/DanceEvent.

    """
    type_: str = Field("DanceEvent", const=True, alias='@type')
    

DanceEvent.update_forward_refs()
