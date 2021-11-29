from pydantic import Field
from pydantic_schemaorg.Event import Event


class DanceEvent(Event):
    """Event type: A social dance.

    See https://schema.org/DanceEvent.

    """

    locals().update({"@type": Field("DanceEvent", const=True)})


DanceEvent.update_forward_refs()
