from pydantic import Field
from pydantic_schemaorg.Event import Event


class BusinessEvent(Event):
    """Event type: Business event.

    See https://schema.org/BusinessEvent.

    """
    type_: str = Field("BusinessEvent", const=True, alias='@type')
    

BusinessEvent.update_forward_refs()
