from pydantic import Field
from pydantic_schemaorg.Event import Event


class LiteraryEvent(Event):
    """Event type: Literary event.

    See https://schema.org/LiteraryEvent.

    """
    type_: str = Field("LiteraryEvent", const=True, alias='@type')
    

LiteraryEvent.update_forward_refs()
