from pydantic import Field
from pydantic_schemaorg.Event import Event


class VisualArtsEvent(Event):
    """Event type: Visual arts event.

    See https://schema.org/VisualArtsEvent.

    """
    type_: str = Field("VisualArtsEvent", const=True, alias='@type')
    

VisualArtsEvent.update_forward_refs()
