from pydantic import Field
from pydantic_schemaorg.Event import Event


class ComedyEvent(Event):
    """Event type: Comedy event.

    See https://schema.org/ComedyEvent.

    """
    type_: str = Field("ComedyEvent", const=True, alias='@type')
    

ComedyEvent.update_forward_refs()
