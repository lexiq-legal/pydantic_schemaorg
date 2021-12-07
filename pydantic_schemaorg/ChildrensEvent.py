from pydantic import Field
from pydantic_schemaorg.Event import Event


class ChildrensEvent(Event):
    """Event type: Children's event.

    See https://schema.org/ChildrensEvent.

    """
    type_: str = Field("ChildrensEvent", const=True, alias='@type')
    

ChildrensEvent.update_forward_refs()
