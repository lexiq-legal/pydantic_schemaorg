from pydantic import Field
from pydantic_schemaorg.Event import Event


class TheaterEvent(Event):
    """Event type: Theater performance.

    See https://schema.org/TheaterEvent.

    """

    locals().update({"@type": Field("TheaterEvent", const=True)})


TheaterEvent.update_forward_refs()
