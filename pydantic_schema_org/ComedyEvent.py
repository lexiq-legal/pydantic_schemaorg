from pydantic import Field
from pydantic_schema_org.Event import Event


class ComedyEvent(Event):
    """Event type: Comedy event.

    See https://schema.org/ComedyEvent.

    """

    locals().update({"@type": Field("ComedyEvent", const=True)})


ComedyEvent.update_forward_refs()
