from pydantic import Field
from pydantic_schema_org.Event import Event


class LiteraryEvent(Event):
    """Event type: Literary event.

    See https://schema.org/LiteraryEvent.

    """

    locals().update({"@type": Field("LiteraryEvent", const=True)})


LiteraryEvent.update_forward_refs()
