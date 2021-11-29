from pydantic import Field
from pydantic_schemaorg.Event import Event


class VisualArtsEvent(Event):
    """Event type: Visual arts event.

    See https://schema.org/VisualArtsEvent.

    """

    locals().update({"@type": Field("VisualArtsEvent", const=True)})


VisualArtsEvent.update_forward_refs()
