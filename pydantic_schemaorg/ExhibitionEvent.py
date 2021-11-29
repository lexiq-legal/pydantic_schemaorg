from pydantic import Field
from pydantic_schemaorg.Event import Event


class ExhibitionEvent(Event):
    """Event type: Exhibition event, e.g. at a museum, library, archive, tradeshow, ...

    See https://schema.org/ExhibitionEvent.

    """

    locals().update({"@type": Field("ExhibitionEvent", const=True)})


ExhibitionEvent.update_forward_refs()
