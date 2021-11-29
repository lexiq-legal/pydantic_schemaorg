from pydantic import Field
from pydantic_schemaorg.Event import Event


class ChildrensEvent(Event):
    """Event type: Children's event.

    See https://schema.org/ChildrensEvent.

    """

    locals().update({"@type": Field("ChildrensEvent", const=True)})


ChildrensEvent.update_forward_refs()
